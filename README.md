# website_assets

### Images:

By default, the image sizes will be set to 100% of the width of the container. If you'd like to change that - consider
using these classes:

* img-small
* img-medium
* img-large

### Code blocks

To use code blocks, we're using Prism. To do the conversion, write code blocks in markdown as such:
```md
<pre><code class="language-sql">SELECT * FROM foo;
SELECT * FROM bar;</code></pre>

```

### Extras:

* Whenever possible, let's convert images to webp format, this will help with page load times. We have a script for
   this.

```python
python
convert_to_webp.py
```

* We are using Prism for our syntax highlighting.
  * We are generating specific languages to reduce the bundle
    size (https://prismjs.com/download.html#themes=prism&languages=sql)
  * We are hosting this on S3
  * Then referencing this in Webflow
