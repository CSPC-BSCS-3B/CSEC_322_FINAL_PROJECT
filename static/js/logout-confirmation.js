/**
 * Handles the logout confirmation modal functionality
 * Prevents accidental logouts during important operations
 */
document.addEventListener('DOMContentLoaded', function() {
    const logoutLink = document.getElementById('logout-link');
    if (logoutLink) {
        logoutLink.addEventListener('click', function(e) {
            e.preventDefault();
            const logoutModal = new bootstrap.Modal(document.getElementById('logoutConfirmationModal'));
            logoutModal.show();
        });
    }
});

/**
 * Session security: Detect if the page is loaded from browser back button after logout
 * This prevents accessing protected content through browser navigation history
 */
if (document.body.classList.contains('logged-in')) {
    window.addEventListener('pageshow', function(event) {
        // If the page is loaded from cache (back button)
        if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {
            // Reload the page to force authentication check
            window.location.reload();
        }
    });
}
