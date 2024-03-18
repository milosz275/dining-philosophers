"""Main module for dining_philosophers package"""

from dining_philosophers.src.feast import Feast

def main():
    """Executes main function"""
    app = Feast()
    app.run()
    return

if __name__ == "__main__":
    main()
