from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rmsApp.models import ReportDetails
from rmsApp.forms import ReportDetailsForm
from django.urls import reverse_lazy

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create your views here.

def indexPage(request):
    response = render(request, 'rmsApp/index.html')
    return response

class ReportDetailsListView(ListView):
    model = ReportDetails
    template_name = "rmsApp/viewReport.html"

    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = context['paginator'].get_page(self.request.GET.get('page', 1))
        return context

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        country = self.request.GET.get('country', '')
        module = self.request.GET.get('module', '')
        edition = self.request.GET.get('edition', '')

        # Start with all reports
        reports = ReportDetails.objects.all()

        # Apply filters based on query parameters
        if query:
            reports = reports.filter(name__icontains=query)
        if country:
            reports = reports.filter(supportedCountry__icontains=country)
        if module:
            reports = reports.filter(module__icontains=module)
        if edition:
            reports = reports.filter(editionNumber=edition)

        return reports

class ReportDetailsCreateView(CreateView):
    model = ReportDetails
    form_class = ReportDetailsForm
    template_name = "rmsApp/addReport.html"
    context_object_name = 'report'
    success_url = reverse_lazy('index')

class ReportDetailsUpdateView(UpdateView):
    model = ReportDetails
    form_class = ReportDetailsForm
    template_name = "rmsApp/editReport.html"
    context_object_name = 'report'
    success_url = reverse_lazy('index')

class ReportDetailsDeleteView(DeleteView):
    model = ReportDetails
    context_object_name = 'report'
    success_url = reverse_lazy('ReportDetails')

# Install ReportLab to download the pdf
# pip install reportlab
def download_catalog_pdf(request):
    # Create the HTTP response with a PDF header
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ReportCatalog.pdf"'

    # Create a PDF canvas
    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle("Report Catalog")

    # Add title to the PDF
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, 750, "Report Catalog")

    # Fetch data from the database
    reports = ReportDetails.objects.all()

    # Table headers
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, 720, "Report Name")
    pdf.drawString(200, 720, "Description")
    pdf.drawString(400, 720, "Country")

    # Draw a line under the header
    pdf.line(50, 715, 550, 715)

    # Add the report data
    y = 700
    for report in reports:
        pdf.setFont("Helvetica", 10)
        pdf.drawString(50, y, report.name)
        pdf.drawString(200, y, report.description[:50])  # Limit description to 50 chars
        pdf.drawString(400, y, report.supportedCountry)
        y -= 20
        if y < 50:  # Start a new page if space runs out
            pdf.showPage()
            y = 750
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(50, y, "Report Name")
            pdf.drawString(200, y, "Description")
            pdf.drawString(400, y, "Country")
            pdf.line(50, y - 5, 550, y - 5)
            y -= 20

    # Finalize the PDF
    pdf.save()
    return response

# TODO: Admin/practitioner login

# TODO: Session menagement
