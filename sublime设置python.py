# 打开"Tools-->Build System-->New Build System"，添加如下内容并保存
{
  "cmd": ["/usr/python3/bin", "-u", "$file"],
  "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
  "selector": "source.python",
  "encoding": "utf-8"
}
