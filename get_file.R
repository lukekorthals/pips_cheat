library(knitr)
library(RCurl)


fileurl <- "https://raw.githubusercontent.com/lukekorthals/pips_cheat/main/OpenBookR.Rmd"
knitrRmd <- paste(readLines(textConnection(getURL(fileurl))), collapse="\n")

setwd("C:/Users/luke-/Desktop/Python Repositories/pips_cheat/")
fn=tempfile()
fn.Rmd <- paste(fn, ".Rmd", sep="")
fn.md <- paste(fn, ".md", sep="")
fn.html <- paste(fn, "-out.html", sep="") 
## Write R Markdown into a file
cat(knitrRmd, file=fn.Rmd)
render_markdown()
knit(fn.Rmd, fn.md)
knit2html(fn.md)
