# Using LaTeX to make graphs

I have been using a bunch of graphing tools, but most of them have some drawbacks and sometimes can hardly meet my needs. For example, Sometimes I'd like to use `mermaid` to make a flowchart or simple graph with code, but you know, this guy doesn't support moving and editing the position of the nodes. And I often use `Excalidraw` to draw some relationship diagrams or some shapes, but it doesn't support the logic operation and you can hardly make an irregular shape or just some a little bit complexer shape.

So, now I'm trying to use LaTeX, which supports a lot of syntax and features.

We use the `TikZ` package to draw pictures, and in fact, what it can do is just forming a PDF file, so we have to convert it to PNG with another tool.

## Install Required Packages

We need to install LaTeX and ImageMagick, which includes tools like `pdflatex` and `convert`. In Ubuntu

```bash
sudo apt update
sudo apt install texlive texlive-pictures texlive-latex-extra imagemagick
```

Waiting for its completion.

## Create a Makeflie

Write a Makefile to automate the compliation process. So we have to let the compiler know what to do. We get the rules here:

```makefile
# 如果没有指定文件，默认使用 example.tex
FILE ?= example.tex

# 提取文件名，不包含扩展名
BASENAME = $(basename $(FILE))

all: $(BASENAME).png

$(BASENAME).pdf: $(FILE)
        pdflatex $(FILE)

$(BASENAME).png: $(BASENAME).pdf
        convert -density 300 $(BASENAME).pdf -quality 90 $(BASENAME).png

clean:
        rm -f $(BASENAME).pdf $(BASENAME).aux $(BASENAME).log

.PHONY: all clean
```

If you type `make` in command line, you will get a bunch of intermediate files, you can take the `tex` file as an example. But you should notice that you cannot get the PNG file here because the compiler will warn you the permission problem.

You should modify the rule manually to permit the generation of PNG.

```bash
sudo vim /etc/ImageMagick-6/policy.xml
```

And find the line:

```diff
- <policy domain="coder" rights="none" pattern="PDF" />
+ <policy domain="coder" rights="read|write" pattern="PDF" />
```

Now there is no problem with generating a PNG file. 

- Using `make` to defaultly generate a PNG file. 
- Using `make clean` to remove the intermediate files.

## Tex file

Here is an example of a Tex file:

```tex
\documentclass{standalone}

\usepackage{tikz}
\usetikzlibrary{automata, positioning, arrows, calc}

\tikzset{
	->,  % makes the edges directed
	>=stealth, % makes the arrow heads bold
	shorten >=2pt, shorten <=2pt, % shorten the arrow
	node distance=3cm, % specifies the minimum distance between two nodes. Change if n
	every state/.style={draw=blue!55,very thick,fill=blue!20}, % sets the properties for each ’state’ n
	initial text=$ $, % sets the text that appears on the start arrow
 }

\begin{document}
	\begin{tikzpicture}
		\node[state with output,accepting, initial] (s0) {$S_0$ \nodepart{lower} $0$};
		\node[state with output, right of=s0] (s1) {$S_1$ \nodepart{lower} $1$};
		\node[state with output, right of=s1] (s2) {$S_2$ \nodepart{lower} $2$};
		\node[state with output, right of=s2] (s3) {$S_3$ \nodepart{lower} $3$};
		\node[state with output, right of=s3] (s4) {$S_4$ \nodepart{lower} $4$};
		\node[state with output, right of=s4] (s5) {$S_i$\nodepart{lower} $\cdots$};
		
		\draw %(s0) edge[loop above] node{$0$} (s0)
			  (s0) edge[bend left] node[above]{$\lambda$} (s1)
			  %
			  (s1) edge[bend left] node[above]{$\lambda$} (s2)
			  (s1) edge[bend left] node[above]{$\mu$} (s0)
			  %
			  (s2) edge[bend left] node[above]{$\lambda$} (s3)
			  (s2) edge[bend left] node[above]{$\mu$} (s1)
			  %
			  (s3) edge[bend left] node[above]{$\lambda$} (s4)
			  (s3) edge[bend left] node[above]{$\mu$} (s2)
			  %
			  (s4) edge[bend left] node[above]{$\lambda$} (s5)
			  (s4) edge[bend left] node[above]{$\mu$} (s3)
			  %
			  (s5) edge[bend left] node{$\mu$} (s4)
		;
	\end{tikzpicture}
\end{document}
```