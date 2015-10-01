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
这样就将learngit文件夹变成了一个repository。设定这个命令后会发现当前目录下出现一个./.git的文件夹，这事git的内部版本控制记录用的文件（默认是隐藏的，想看可以用 ls -ah），不懂不要改，也不需要改。

	设定完成后就可以在learngit中放入文件或改动文件了。改动后需要提交改动记录给 ”云记事本 “ ，这时候会用两个指令 (例如增加了一个readme.txt 文件）：
git add readme.txt
git commit -m "I add a txt file"
	git add命令是用于将 readme.txt放到repository中，因为readme.txt在learngit目录下并不以为着这个文件就 “ 过户 ” 到仓库中，就像仓库是一个快递站点，现在运来了一批快递放在这个站点中，在快递员没有在相应快递上签字签收前，这些快递都不属于这个站点，这样发错的快递和隔壁老奶奶放在这的大葱就都仅仅是暂时放在这里，不会入库存放。
	git commit 命令是将放在repository中的文件提交导git。这是什么意思呢？并且这个和add命令有什么区别？ commit命令将文件提交git中并不是真正的提交文件本身或者其副本。git是一个分布式的文件管理系统，与集中式文件管理系统不同，分布式管理系统的没有所谓的中央服务器，文件不是由一个总服务器存储，而是由各个小站点存储。而git提交的是文件更改的信息，什么是信息，就是我更改了哪个文件中的那几行（视频，图片或者word这种二进制文件无法详细知道哪些行更改）。git的服务器就不是像集中式管理系统那样存储文件了，而是像一个公告牌，上面列出了文件的变动信息。这时候当别人需要更新文件时，用户通过键入命令，站点的git软件就会查询git公告牌中的更新信息，然后根据信息去请求存放更新文件的那个站点，从那里取回更新的文件。 -m是 commit的一个参数，用于加入更新信息的说明，这里更新的信息说明是"I add a txt file"，可以没有说明直接提交更改文件，命令还没查。
