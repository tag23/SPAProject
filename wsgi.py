from server.application import create_app

app = create_app()

if __name__ == "__main__":
    print("Hosting server!")
    app.run(debug=False)
