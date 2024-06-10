import requests


# Slight mod from this: https://gist.github.com/waterrmalann/7318e61de34341a3c3bf9964e144c547
def minify_html(html_file, overwrite=False):
    with open(html_file, 'r') as f:
        html = f.read()

    req = requests.post('https://www.toptal.com/developers/html-minifier/api/raw', {'input': html})

    save_path = html_file if overwrite else html_file[:-5] + '.min.html'
    with open(save_path, 'w') as f:
        f.write(req.text)


minify_html('body.html')
minify_html('head.html')
