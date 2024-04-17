# 定义源文件和目标文件夹
SRC = $(wildcard *.md)
OBJ = $(patsubst %.md,public/%.html,$(SRC))

# 默认目标
all: $(OBJ)

# 确保public文件夹和CSS文件存在
public: public/style.css
	mkdir -p public

# 目标文件夹
public/%.html: %.md public/style.css | public
	pandoc $< -o $@ --template template.html --standalone --from markdown --to html --highlight-style=tango

# 复制CSS文件到public文件夹
public/style.css: style.css
	cp $< $@
# 清理生成的文件
clean:
	rm -f public/*.html public/style.css

.PHONY: all clean

