import os
from src.data_loader import load_data
from src.preprocess import preprocess
from src.trainer import train_model
from src.evaluator import evaluate
from src.visualizer import plot_delay_by_route

def main():
    df = load_data(os.path.join(os.path.dirname(__file__), '..', 'data', 'transport_delay.csv'))
    X_train, X_test, y_train, y_test = preprocess(df)
    model = train_model(X_train, y_train)
    acc, report = evaluate(model, X_test, y_test)
    print("Accuracy:", acc)
    print(report)
    plot_delay_by_route(df)

if __name__ == "__main__":
    main()
