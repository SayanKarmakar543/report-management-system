document.addEventListener('DOMContentLoaded', function () {
    const deleteModal = document.getElementById('deleteModal');
    const reportNameElement = document.getElementById('reportName');
    const deleteForm = document.getElementById('deleteForm');

    deleteModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        const reportId = button.getAttribute('data-id');
        const reportName = button.getAttribute('data-name');

        // Update modal content
        reportNameElement.textContent = reportName;

        // Set the form action dynamically to target the correct report
        deleteForm.action = `/delete-report/${reportId}/`;  // Adjust the URL pattern to match your delete view
    });
});