mkdir -p ~/.streamlit/

echo -e "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
primaryColor = '#d33682'\n\
backgroundColor = '#002b36'\n\
secondaryBackgroundColor = '#586e75'\n\
textColor = '#fafafa'\n\
font = 'sans serif'" > ~/.streamlit/config.toml


