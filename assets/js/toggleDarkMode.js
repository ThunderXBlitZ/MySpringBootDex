const changeTheme = document.getElementById('mode');

// on page load
const mode = window.localStorage.getItem('mode');
if (mode == 'dark') {
  changeTheme.checked = true;
  jtd.setTheme("mydarktheme");
}

if (mode == 'light') {
  changeTheme.checked = false;
  jtd.setTheme("mytheme");
}

// toggles dark mode
const theme = document.getElementById('theme');
changeTheme.onchange = (e) => {
  if (changeTheme.checked === true) {
    jtd.setTheme("mydarktheme")
    window.localStorage.setItem('mode', 'dark');
  } else {
    jtd.setTheme("mytheme")
    window.localStorage.setItem('mode', 'light');
  }
}