# packages

![Alt text](https://cdn.activestate.com/wp-content/uploads/2020/04/python-list-packages.png"a title")



## 1 NumPy
You can do basic mathematical operations without any special Python packages. However, if you’re going to do any kind of complex math, the NumPy package will make your coding life much easier.

NumPy provides tools to help build multi-dimensional arrays and perform calculations on the data stored in them. You can solve algebraic formulas, perform common statistical operations, and much more.

While NumPy is a valuable Python package for a variety of general-purpose programming tasks, it’s particularly important if you want to do machine learning, since it provides part of the foundation for libraries like TensorFlow.


## 2 Pendulum
If you have at least a little Python programming experience, you probably know that you can use the datetime module to manage dates and times within an application.

While datetime is great for basic work along these lines, the Pendulum Python package makes it easier to do more complex coding involving dates and times. It’s more intuitive to work with, and it manages time zones automatically.

Best of all, Pendulum is designed to be a drop-in replacement for datetime. That means you can use it with code you’ve already written based on datetime. With only a few exceptions, Pendulum will work just as well, without the need to modify the code, while providing extra features not present in plain-old datetime.


## 3 Python Imaging Library
If your Python application interacts with images in any way, the Python imaging library, also known as PIL or Pillow, is a Python must-have. It makes it easy to write code that opens, modifies, and saves images in a variety of formats.

If you’re doing more advanced work with images (like image recognition, in which case OpenCV would be a good package to consider), Pillow won’t cut it on its own. But for basic image importing, manipulation, and exporting, Pillow is your go-to solution.

## 4 MoviePy
MoviePy is to videos what Pillow is to images. It provides a range of functionality for common tasks associated with importing, modifying, and exporting video files. It also lets you do things like insert titles into videos or rotate videos 90 degrees (if for some reason you decide you want to do that).

Like Pillow, MoviePy is not intended as a tool for advanced data manipulation. If you’re writing a video editing app, you’ll probably also need to rely on OpenCV (which can work with videos as well as images) to provide the advanced functionality that MoviePy lacks. But for most standard tasks involving videos in Python code, MoviePy gets the job done quite well.


## 5 Requests
Writing code that sends HTTP requests can be tricky, due in no small part to the fact that HTTP does not exactly format data in a way that is easy for humans to read.

The Requests Python package (motto: “HTTP for Humans”) tackles this problem by automating many of the tedious tasks that you would otherwise need to perform in order to send HTTP requests from your application. It removes the need to add query strings, or do POST form encoding. It also keeps connections with HTTP servers alive automatically, eliminating the need to write a bunch of code for doing that.

In short, if your application sends any data over HTTP, Requests is a must-have package.


## 6 Tkinter
Want to develop a Python app with a Graphical User Interface (GUI)? There are a variety of packages designed to help you do that (indeed, we could make a top ten list of just Python GUI packages). But I think most Python developers would agree that Tkinter is the most important — and most commonly used — framework for creating GUIs. It binds Python to the TK GUI toolkit, which works on virtually every modern operating system.

Unless you have a strong preference for a different GUI toolkit, Tkinter is probably the best place to start when creating a Python GUI.


## 7 PyQt
The preceding sentence notwithstanding, PyQT, another Python package for building GUIs, is also a strong contender. It provides bindings to (you guessed it) the Qt toolkit, which is also cross-platform. It’s intended for heavier-duty GUI programming than Tkinter. That means that PyQT may be overkill if you’re building an app that has a pretty simple interface — say, just a window with some buttons and text fields — but it is a good tool if you want to build a complex, multi-dimensional GUI.


## 8 Pandas
There is a long list of Python packages designed for working with complex data sets. But arguably, Pandas is the most important. Pandas helps you manipulate and analyze large sets of data without having to learn a specialized data-processing language like R.

Pandas has its limits in that it’s not intended for advanced statistical modelling (in that case, you would want to learn R, or use a Python package like statsmodels). But if you need to do things like process time-series data or perform statistical analysis on a data set, Pandas has you covered.

## 9 Pywin32
For Windows Python programming in particular, Pywin32 is a must-have package. It provides access to many of the native Windows API functions, allowing you to do things like interact with the Windows registry, use the Windows clipboard, and much more.

Pywin32 won’t do you much good if you’re building a cross-platform Python app, but Windows developers might find that they like it so much that they use it instead of native Windows tooling.

 

 ## 10 Pytest
If you have a Python development project of any complexity, being able to perform testing on new code is essential. The Pytest package provides a variety of modules to help you do this. Whether it’s a simple unit test or a more complex functional test, Pytest can help you write it.

 

 