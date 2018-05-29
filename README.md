# dailyfresh
django project
只是根据bilibili上少有的视频，加自己的少部分创作
功能不是很多...
在uwigi上部署 是拷贝别人的代码

	创建django框架
		django-admin startproject dailyfresh
		
	settings设置数据库基本信息
		数据库name, password, engine, host, port等等
		在mysql中创建对应的数据库
		
	static设置静态文件配置
		os.path.join(BASE_DIR, 'static') //定义static在项目根目录
		
	templates设置
		在DIR_list中添加 
		os.path.join(BASE_DIR, 'templates') //放置网页的文件夹
		
	创建df_user用户app //用户
		django-admin startapp df_user
		
	编写df_user的model.py文件
		定义UserInfo(models.Model)类
		添加 uname, upwd, uphone, uzipcode, utaker, uemail, uaddress等等
		
	命令行：
		python manager.py makemigrations 创建migrations初始化
		python manager.py migrate  		 在数据库中创建对应的table表
    
 货物需要自己手动输入
	 
