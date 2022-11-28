mkdir -p ~/.streamlit/
echo "\
[general]\n\
email=\"kumaria2001@gmail.com\"\n\
" > ~/.streamlit.toml

echo"\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
"> ~/.streamlit/config.toml
