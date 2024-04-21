'''
这个脚本在执行时会自动跳转到目标目录，并统计该目录下所有markdown文件的字数
但是需要注意的是，脚本并不会全局改变shell的路径，在执行完成后会停留在原来的路径下
这里find因为权限原因只会检查几个目录: Documents, Documents, Desktop
然后我们希望这个脚本在每次提交的时候都能执行一次，我们需要找到`.git/hooks/pre-commit`文件，如果没有，则进行cp操作:
cp pre-commit.sample pre-commit
并在其中添加下面这一条命令：
find ~/Documents ~/Downloads ~/Desktop -path '*/Musings/word_count.py' | xargs python
寻找这个脚本文件路径的方法：
1. 使用正则表达式: find ~/Documents ~/Downloads ~/Desktop -path '*/Musings/word_count.py'
2. 寻找两次: find ~/Documents ~/Downloads ~/Desktop -name "Musings" -exec find {} -type f -name "word_count.py" \;
'''
import os
import sys
import re
import subprocess
import platform

def detect_os():
    system = platform.system()
    if system == 'Darwin':
        return "macOS"
    elif system == 'Linux':
        return "Linux"
    else:
        return "未知操作系统"

# 跳转到目标目录，前提是该目录名称在目标文件夹下只能有一个，否则只会跳转到第一个
def change_dir(target: str):
    try:
        # 使用find命令找到目标目录
        if detect_os() == "macOS":
            find_command = f"find ~/Documents ~/Downloads ~/Desktop -type d -name {target}"
        elif detect_os() == "Linux":
            find_command = f"find ~ -type d -name {target}"
        else:
            return sys.exit(1)

        result = subprocess.run(find_command, capture_output = True, text = True, shell = True)
        if result.returncode != 0:
            print("命令执行出错:")
            print(result.stderr)
            sys.exit(1)
        # 若正常执行，获取输出中的第一个匹配项
        paths = result.stdout.split('\n')
        if paths:
            path = paths[0]
            os.chdir(path)
        else:
            print(f"未找到{target}目录")
            sys.exit(1)
    except Exception as e:
        print(f"切换目录时发生错误: {e}")
        sys.exit(1)

# 检查当前目录，如果不是目标目录则自动跳转
def check_directory():
    current_dir = os.getcwd()
    if not re.search(r'.*/Musings$', current_dir):
        print("当前shell路径不在该目录下，正在切换至文件目录...")
        change_dir("Musings")
        print("切换成功")

def count_words():
    # 检测当前路径下所有markdown文件的字数
    total_words = 0
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding = 'utf-8') as f:
                    contents = f.read()
                    words = contents.split()
                    total_words += len(words)
    return total_words

def update_readme(total_words):
    readme_path = os.path.join(os.getcwd(), 'README.md')
    with open(readme_path, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
    lines[2] = f"目前我已经写了：| **{total_words}** | 字\n"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

if __name__ == '__main__':
    check_directory()
    words = count_words()
    print(f"当前全部字数: {words}")
    update_readme(words)
