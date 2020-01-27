# Resumes and Portfolios for Data Science
*Anders Poirel,  27-01-2020*

## Resume

LaTeX is a great tool for writing clean, consistently styled resumes.

### Setting up LateX

You can use [Overleaf](https://www.overleaf.com/), but long-term a local set-up will make your life easier.

#### Distribution

##### Windows
[TeXLive](https://www.tug.org/texlive/) is the easiest way as it comes with **all** the packages though it's a hefty install (~10GB). Otherwise, look into [MikTeX](https://miktex.org/).

##### MacOS

[TexLive](https://www.tug.org/texlive/) is the easiest way as it comes with **all** the packages though it's a hefty install (~10GB). Otherwise, look into [MacTeX](https://tug.org/mactex/).

#### Editor
You can use a LaTeX-specific IDE, but the easiest and best way is probably just to install a LaTex plugin for your preferred text editor:
- VS Code: [https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
- Atom:[https://atom.io/packages/atom-latex](https://atom.io/packages/atom-latex)
- vim: [http://vim-latex.sourceforge.net/](http://vim-latex.sourceforge.net/)
- Sublime Text: [https://latextools.readthedocs.io/en/latest/](https://latextools.readthedocs.io/en/latest/)

If you don't know LaTeX syntax, a good tutorial is the 
[Not So Short Introduction to Latex](https://tobi.oetiker.ch/lshort/lshort.pdf). For specific questions, [Latex Stack Exchange](https://tex.stackexchange.com/) and Overleaf's documentation are useful.

### Making a Resume

Make sure `res.cls` is in the same directory as your resume (you'll need to upload it if on Overleaf).

A good starting point is the templates on 
[https://www.rpi.edu/dept/arc/training/latex/resumes/](https://www.rpi.edu/dept/arc/training/latex/resumes/) - adapt the `.tex` file associated to the one that looks best to you.


### Portfolio

How to make a good portfolio:
- Explain your work in 1-2 sentences
- Include some sort of metric (at least in the main ones)
- Include links to the repository (and live project if relevant)
- Detail the main technologies used
- The linked repo should be well-structured and have an informative README

Data Science specific tips:
- Show evidence of good SWE practices (read [Cookie Cutter Data Science](https://drivendata.github.io/cookiecutter-data-science/))
- Include a report with approaches attempted, strategies used to increase performance and evaluation
- Incude a nice data visualization/exploration in another notebook
- Notebooks are for exploration, reports and presentation. Code re-used across a project and generating final predictions/models should not be in a notebook

#### Examples
Neither of these are perfect! I wasn't aware of some of these guidelines a few months ago 🙂.
- Github: [https://github.com/Jswig/Project-Portfolio/blob/master/README.md](https://github.com/Jswig/Project-Portfolio/blob/master/README.md)
- Website: [https://www.julianlehrer.me/html/projects.html](https://www.julianlehrer.me/html/projects.html)


## Credits

*Using Latex Resume Templates*, [Rensselaer Career Development Center](https://www.rpi.edu/dept/arc/training/latex/resumes/), 2007