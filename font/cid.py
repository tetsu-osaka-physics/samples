a = [s for s in range(10)]

with open('cid.tex', 'w') as f:
    print("\\documentclass[a4paper, papersize, dvipdfmx, bold, twocolumn]{jsarticle}\n\\usepackage{otf}\n\\begin{document}", file=f)
    print("\\makeatletter\\def\\@hexadecimal#1{\\ifcase#1\\or 0\\or 1\\or 2\\or 3\\or 4\\or 5\\or 6\\or 7\\or 8\\or 9\\or A\\or B\\or C\\or D\\or E\\or F\\else\\@ctrerr\\fi\\relax}", file=f)
    print("\\def\hexadecimal#1{\expandafter\@hexadecimal\csname c@#1\endcsname}", file=f)
    print("\\renewcommand\\thesection{\\bfseries\\hexadecimal{section}\#\#\#\#}", file=f)
    print("\\renewcommand\\thesubsection{\\bfseries\\hexadecimal{section}\\hexadecimal{subsection}\#\#\#}", file=f)
    print("\\renewcommand\\thesubsubsection{\\bfseries\\hexadecimal{section}\\hexadecimal{subsection}\\hexadecimal{subsubsection}\#\#}", file=f)

    for i in range(2):
        print("\n\\section{}", file=f, sep='')
        for j in range(10):
            print("\n\\subsection{}", file=f, sep='')
            for k in range(10):
                print("\n\\subsubsection{}", file=f, sep='')
                for l in range(10):
                    print("\\par\n", file=f)
                    for m in range(10):
                        print("\\CID{", a[i], a[j], a[k], a[l], a[m], "}", file=f, sep='')

    print("\n\\end{document}", file=f)
