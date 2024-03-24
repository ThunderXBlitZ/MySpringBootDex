const changeTheme = document.getElementById('mode');

// on page load
const mode = window.localStorage.getItem('mode');
if (mode != null && mode == 'dark') {
  changeTheme.checked = true;
} else {
  changeTheme.checked = false;
}

function toggleDarkMode(){
  if (changeTheme.checked === true) {
    jtd.setTheme("mydarktheme")
    window.localStorage.setItem('mode', 'dark');
    document.body.style.setProperty("--labelColor", "#7253ed")
  } else {
    jtd.setTheme("mytheme")
    window.localStorage.setItem('mode', 'light');
    document.body.style.setProperty("--labelColor", "#DC143C")
  }
}
// toggles dark mode
const theme = document.getElementById('theme');
changeTheme.onchange = (e) => {toggleDarkMode()};

toggleDarkMode();