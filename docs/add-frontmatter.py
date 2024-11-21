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
    search_flag = False
    for line in html:
        modified_line = None

        # make the links at the bottom of index.html work
        if "<li><a href=" in line:
            if (
                '<li><a href="../index.html">Documentation overview</a><ul>'
                in line
            ):
                modified_line = (
                    '<li><a href="./index.html">Documentation overview</a><ul>'
                )
            else:
                modified_line = (
                    line.replace("/", ".")
                    .replace("<.a>", "</a>")
                    .replace("<.li>", "</li>")
                )
        else:
            if (
                '<li class="toctree-l1"><a class="reference internal" href="../gem5.html">gem5 package</a></li>'
                in line
            ):
                print("../gem5.html switched to ./gem5.html")
                modified_line = '<li class="toctree-l1"><a class="reference internal" href="./gem5.html">gem5 package</a></li>'

            elif (
                '<h1 class="logo"><a href="../index.html">gem5</a></h1>'
                in line
            ):
                print("../index.html switched to ./index.html")
                modified_line = (
                    '<h1 class="logo"><a href="./index.html">gem5</a></h1>'
                )
            else:
                # remove the search bar
                if "<search" in line:
                    search_flag = True
                    modified_line = ""
                elif "</search>" in line:
                    search_flag = False
                    modified_line = ""
                elif search_flag == True:
                    modified_line = ""
                else:
                    modified_line = line
        f.write(modified_line)
        print("latest version gotten")
for filename in os.listdir("./_build/html"):

    # print(filename)
    if filename.startswith("gem5"):  # and filename != "gem5.html"
        # print(filename)
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
