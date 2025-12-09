// Toggle Chat Widget
function toggleChat() {
    const widget = document.getElementById('chatWidget');
    const icon = document.getElementById('toggleIcon');
    
    widget.classList.toggle('minimized');

    if (widget.classList.contains('minimized')) {
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-up');
    } else {
        icon.classList.remove('fa-chevron-up');
        icon.classList.add('fa-chevron-down');
    }
}

// Open Chat when clicking an item
function openChatWithItem(itemName) {
    const widget = document.getElementById('chatWidget');
    if (widget.classList.contains('minimized')) {
        toggleChat();
    }
    // You could theoretically pass the item name to the bot here if using custom JS bridge,
    // but for iframe, opening it encourages the user to type.
}

// Ensure it starts minimized
document.addEventListener('DOMContentLoaded', () => {
    const widget = document.getElementById('chatWidget');
    if (!widget.classList.contains('minimized')) {
        widget.classList.add('minimized');
    }
});