from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():   
    nav = """
    <nav>
        <a href="#">Home</a>
        <a href="/classes">Classes</a>
        <a href="/objects">Objects</a>
        <a href="/about">About</a>
    </nav>
    """
    
    title = "<h1>Classes and objects</h1>"

    content = """
        <h3>Classes are the templates that objects use when they are created</h3>
        <p>A class is like a definition, that will specify how an object will be constructed but it is not the object itself, classes include a constructor, fields and methods.</p>
        <p>An object is an instance of a class created with the constructor, its methods and fields will be accesible and when instantiated it will allocate a space in memory.</p>
    """

    table = """
        <table>
            <tr>
                <th>Classes</th>
                <th>Objects</th>
            </tr>
            <tr>
                <td>Represents a template for an object</td>
                <td>It's an instance of a class</td>
            </tr>
            <tr>
                <td>Doesn't allocate memory</td>
                <td>Allocates memory space</td>
            </tr>
            <tr>
                <td>Can't be manipulated because it doesn't exist in memory</td>
                <td>Can be manipulated</td>
            </tr>
            <tr>
                <td>Doesn't have values associated with its fields</td>
                <td>Every object has its own values associated with it</td>
            </tr>
        </table>
    """
    return nav + title + content + table


@app.get("/classes")
def classes():
    nav = """
    <nav>
        <a href="/">Home</a>
        <a href="#">Classes</a>
        <a href="/objects">Objects</a>
        <a href="/about">About</a>
    </nav>
    """
    
    title = "<h1>Classes</h1>"

    content = """
        <p>Classes are to objects, like blueprints are to houses, it defines the structure for the creation of an object.</p>
        <p>A class includes properties which hold data, it has its own methods and has a constructor which sets initial values for the object.</p>
        <h3>Python Example</h3>
        <p>class Person:<br>
                    &nbsp def __init__(self, name, age):<br>
                        &nbsp &nbsp &nbsp self.name = name<br>
                        &nbsp &nbsp &nbsp self.age = age<br>
                    <br>
                    &nbsp def myfunc(self):<br>
                        &nbsp &nbsp &nbsp print("Hello my name is " + self.name)</p>
        <p>The <i>__init__</i> function in a class will execute when a class is being used to create an object object.</p>
        <p>The keyword <i>self</i> refers to the instance of the class, we use it to access variables that belong to that class.</p>
    """
    return nav + title + content


@app.get("/objects")
def objects():
    nav = """
    <nav>
        <a href="/">Home</a>
        <a href="/classes">Classes</a>
        <a href="#">Objects</a>
        <a href="/about">About</a>
    </nav>
    """

    title = "<h1>Objects</h1>"

    content = """
        <p>Objects are instances of classes, so depending on the class used to create the object, it will define the methods and properties that it will have.</p>
        <p>Each object will hold its own values however, they will be accesed the same way but their values will not be the same as they take different space in memory.</p>
        <br>

        <h2>How to create an object</h2>
        <p>First off, you need to have a class defined in your code, then just like creating a new variable you will set it to equal to a Class along with the values for it (if needed), for example:
        <p>class MyClass:<br>
                &nbsp def __init__(self, name):<br>
                    &nbsp &nbsp &nbsp self.name = name<br>
                <br>
                &nbsp def hello(self):<br>
                    &nbsp &nbsp &nbsp print("Hello " + self.name + "!")<br>
            <br>
            <b>myObject = MyClass("Jorge")</b></p>
        <p>This will create a myObject object using the MyClass blueprint, so it will contain a property called "name" and a method called "hello".</p>
        <br>

        <h2>Access object properties</h2>
        <p>You can access an object's property to read it or change its value.</p>
        <p>name = myObject.name <b>#READ</b></p>
        <p>myObject.name = "David" <b>#WRITE</b></p>
        <br>

        <h2>Call methods</h2>
        <p>Just like accessing a property but remember to pass parameters needed for the method, if it doesn't have parameters it will be an empty (). Remember, if the method uses <i>self</i> you don't need to pass a parameter for that.</p>
        <p>myObject.hello()</p>
        <p>Hello Jorge!</p>
    """

    return nav + title + content


@app.get("/about")
def about():
    nav = """
    <nav>
        <a href="/">Home</a>
        <a href="/classes">Classes</a>
        <a href="/objects">Objects</a>
        <a href="#">About</a>
    </nav>
    """

    title = "<h1>About Me</h1>"

    content = """
        <h3>Hello, I am Jorge Tostado, I made this simple web app by using Python and Flask!</h3>
        <p>I'm a 21 years old, currently a student in computer systems engineering, very passionate about programming and I love computers, as of now I'm going through SDGKU's Full Stack course and learning stuff like HTML and databases!</p>
        <p>In my off time I like playing lots of video games like Splatoon and Stardew Valley or watching people play other kinds of games on Twitch.</p> 
    """
    
    return nav + title + content