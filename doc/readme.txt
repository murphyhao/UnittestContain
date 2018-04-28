# 初始化提交
git init
git config --global user.email "ecd1393@163.com"
git commit -m "first commit"
git remote add origin https://github.com/murphyhao/UnittestContain.git
git push -u origin master

# 初始化下载
git remote add origin https://github.com/murphyhao/UnittestContain.git
git pull origin master

# 删除文件夹（.vscode文件夹为例）
git rm -r --cached .vscode  #--cached不会把本地的.vscode删除
git commit -m 'delete .vscode dir'
git push -u origin master