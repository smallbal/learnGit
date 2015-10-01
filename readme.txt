Git is a version control system.
And I think Git is so fucking difficult to learn now :(

安装git
用 sudo apt-get install git 进行安装，用源码包安装的方法我还没成功，原因是没看懂说明中的那三个步骤： ./config ---> make ---> makeall

git 在使用前要进行一些设置：
sudo git config --global user.name"You Name" #设置你使用git是的“昵称”
sudo git config --global user.email"You E-mail" #设置你的E-mail
这两句必须要有 ，其中--global 参数表示这两个设置应用与git的全局，当需要对某一个“仓库”进行特殊设定时再单独设定。如果没有这两个设定则对git后面的操作将会受限制。


