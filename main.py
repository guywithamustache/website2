"""module docstring"""
from website import create_app

#create object of create_app
app = create_app()

#so I can just refresh the page to run the website
if __name__ == '__main__':
    app.run(debug=True)
