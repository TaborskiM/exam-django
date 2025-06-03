document.addEventListener('DOMContentLoaded', function() {
  // Applique le thème au chargement
  applyTheme(localStorage.getItem('adminTheme') || '4');
  
  // Mutation GraphQL pour changer le thème
  window.changeAdminTheme = function(themeId) {
    fetch('/graphql/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({
        query: `mutation ($themeId: ID!) {
          switchTheme(themeId: $themeId) {
            success
            activeTheme { id name }
          }
        }`,
        variables: { themeId }
      })
    })
    .then(res => res.json())
    .then(data => {
      if (data.data?.switchTheme?.success) {
        applyTheme(data.data.switchTheme.activeTheme.id);
       
      }
    });
  };

  function applyTheme(themeId) {
    const themeClass = themeId === '4' ? 'light' : 'dark';
    document.body.setAttribute('data-theme', themeClass);
    localStorage.setItem('adminTheme', themeId);
    
    // Force le recalcul des styles
    document.body.style.display = 'none';
    document.body.offsetHeight; // Trigger reflow
    document.body.style.display = '';
  }

  function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
});


