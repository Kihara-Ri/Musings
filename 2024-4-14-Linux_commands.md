# Linux Commands

## Preface

If you want to be efficient when you are working with Linux operating system, using Linux commands lines proficiently is really necessary. You may think that wtf there are so many Linux commands with countless parameters and it’s almost impossible for you to remember all of those. In fact, if we just make good categorization and look up to the **manual**, that won’t be a really tough job.

## Start

There have been so many sites and curriculums on the Internet for you to search, so if you are stuck, Google search usually does the trick.

Common commands

- File managing: `cd`, `pwd`, `mkdir`, `rmdir`, `ls`, `cp`, `rm`, `mv`, `tar`
- Data wrangling: `cat`, `more`, `less`, `head`, `tail`, `file`, `find`
- IO: pipe`|`, redirect, `tee`, `xargs`
- Text operating: `vim`, `grep`, `awk`, `sed`, `sort`, `wc`, `uniq`, `cut`, `tr`
- Regex
- System monitoring: `jobs`, `ps`, `top`, `kill`, `free`, `dmesg`, `lsof`, `df`

---

`ls`, with some arguments `-l`, `-a`, `-h` used a lot.

`file`,  tells you the kind certain data is. In Linux, everything is a file so you can detect anything using this command.

`less` to look up the texts.

`mkdir` to make a new directory, `make directory`

`>`, if you straightly use this to link files, you’ll redirect the following content in to this file, but you should notice that `>` would do **overwrite** operation, and the existing content would be deleted.

`>>`, if you want to append something, you’re going to use this.

`<`: you receive the data.

---

`type`: Used to get to know other commands

Some tough cases may be the following commands:

- `grep`
- `sed`
- `sort`

## A little challenge

This is a little challenge from the missing semester of MIT [Lecture 1: Course Overview + The Shell](https://missing-semester-cn.github.io/2020/course-shell/)

1. Create a new directory called `missing` under `/tmp`.
2. Look up the `touch` program.
3. Use `touch` to create a new file called `semester` in `missing`.
4. `Write` the following into that file, one line at a time:

```bash
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu
```

5. Try to execute the file, i.e. type the path to the script (`./semester`) into your shell and press enter.
6. Use `|` and `>` to write the “last modified” date output by `semester` into a file called `last-modified.txt` in your home directory.
7. Write a command that reads out your laptop battery’s power level or your desktop machine’s CPU temperature from `/sys`.

My operation:
```bash
mkdir /tmp/missing
touch /tmp/missing/semester && cd /tmp/missing/
echo "#\!/bin/sh\ncurl --head --silent https://missing.csail.mit.edu" > semester
chmod +x semester
ls -l $_
./semester | grep last-modified > last-modified.txt
--> last-modified: Sat, 02 Mar 2024 14:52:48 GMT

cat /sys/class/power_supply/BAT1/capacity
--> 100
```

Just a heads-up, I used the double quotes `""` instead of the quotes `''` so that I can take advantage of the backslash `\` feature, and specifically I use `\n` to perform a newline operation.



