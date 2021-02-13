from main import create_app
import sys

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=sys.argv[1])