Git is a version control system.
And I think Git is so fucking difficult to learn now :(

安装git
用 sudo apt-get install git 进行安装，用源码包安装的方法我还没成功，原因是没看懂说明中的那三个步骤： ./config ---> make ---> makeall

	git 在使用前要进行一些设置：
sudo git config --global user.name"You Name" #设置你使用git是的“昵称”
sudo git config --global user.email"You E-mail" #设置你的E-mail
这两句必须要有 ，其中--global 参数表示这两个设置应用与git的全局，当需要对某一个“仓库”进行特殊设定时再单独设定。如果没有这两个设定则对git后面的操作将会受限制。

	在安装和设置好git后，就可以使用git了。git形象的说是用于创建一个 个“云仓库”，我们可以在这些仓库中修改，加入或删除文件，然后将这些变化信息上传网络，于是在别处的运仓库就可以通过命令查询到这些变化，如果别的仓库需要这些变化，就可以从改动的仓库中调动文件过来，这样新仓库的文件就得以更新。

	git中的仓库称为 “repository” ，git的所有改动都必须在已有的仓库目录中进行。在PC中没有repository时，可以：
mkdir learngit
cd ./learngit
创建一个文件夹 learngit并切入。随后使用：
git init
这样就将learngit文件夹变成了一个repository。
 
