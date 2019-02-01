import argparse
import pandas as pd
from pipeline import *

# Main script which calls other model functions.

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A script which utilizes a model trained on the dataset {{ dataset }} to predict {{ target }}.'
                    'Script created using automl-gs.')
    parser.add_argument('-d', '--data',  help='Input dataset (must be a .csv)')
    parser.add_argument(
        '-m', '--mode',  help='Mode (either "train" or "predict")')
    parser.add_argument(
    '-s', '--split',  help='Train/Test Split (if training)',
    default=0.7)
    parser.add_argument(
    '-e', '--epochs',  help='# of Epochs (if training)',
    default=20)
    args = parser.parse_args()

    df = pd.read_csv(args.data)
    data_tf = transform_data(df)

    {# TensorFlow builds the model and loads weights. #}
    model = build_model()

    if args.mode == 'predict':
        model.load_weights('model_weights.hdf5')


    if args.mode == 'train':
        model_train(data_tf, model)
    elif args.mode == 'predict':
        predictions = model_predict(data_tf, model)
        pd.DataFrame(predictions).to_csv('predictions.csv', index=False)
