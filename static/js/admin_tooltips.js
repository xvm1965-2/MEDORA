// static/js/admin_tooltips.js
document.addEventListener('DOMContentLoaded', function() {
  const helpIcons = document.querySelectorAll('.help-icon');
  
  helpIcons.forEach(icon => {
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = icon.dataset.helpText;
    tooltip.style.display = 'none';
    document.body.appendChild(tooltip);
    
    icon.addEventListener('mouseenter', (e) => {
      const rect = icon.getBoundingClientRect();
      tooltip.style.left = `${rect.right + window.scrollX}px`;
      tooltip.style.top = `${rect.top + window.scrollY}px`;
      tooltip.style.display = 'block';
    });
    
    icon.addEventListener('mouseleave', () => {
      tooltip.style.display = 'none';
    });
  });
});