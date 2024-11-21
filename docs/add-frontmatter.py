import os

# for filename in os.listdir('../../docs/_build/html'):
# for filename in os.listdir('/Volumes/Crucial/gem5-dev/website/_pages/documentation/general_docs/sphinx_docs'):

with open(f"./_build/html/_modules/index.html", "r+") as f:
    html = f.readlines()
    f.seek(0, 0)
    f.write("---\n")
    f.write(f'title: "Sphinx Documentation"\n')
    f.write("parent: sphinx-docs\n")
    f.write(f"permalink: /documentation/general_docs/sphinx_docs/index.html\n")
    f.write("---\n")
    # f.write(html)
    for line in html:
        if "<li><a href=" in line:
            modified_line = line.replace("/", ".").replace(
                "<.a><.li>", "</a></li>"
            )
            f.write(modified_line)
        else:
            f.write(line)

for filename in os.listdir("./_build/html"):

    print(filename)
    if filename.startswith("gem5"):  # and filename != "gem5.html"
        print(filename)
        # with open (f"../../docs/_build/html/{filename}", "r+") as f:
        # with open (f"/Volumes/Crucial/gem5-dev/website/_pages/documentation/general_docs/sphinx_docs/{filename}", "r+") as f:
        with open(f"./_build/html/{filename}", "r+") as f:
            html = f.read()
            f.seek(0, 0)
            f.write("---\n")
            f.write(f'title: "{filename}"\n')
            f.write("parent: sphinx-docs\n")
            # modified_filename = filename.replace(".", "/").replace(
            #     "/html", ".html"
            # )

            # f.write(
            #     f"permalink: /documentation/general_docs/sphinx_docs/{modified_filename}\n"
            # )
            f.write(
                f"permalink: /documentation/general_docs/sphinx_docs/{filename}\n"
            )
            f.write("---\n")
            f.write(html)
