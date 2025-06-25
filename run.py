from heyapp import create_app

# For development, you might call it directly
if __name__ == '__main__':
    app = create_app('../config.py') # Adjust path as needed
    app.run(debug=True)
