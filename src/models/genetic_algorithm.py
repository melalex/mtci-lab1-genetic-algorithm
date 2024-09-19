import tensorflow as tf
import tensorflow_probability as tfp
import pandas as pd
import keras
from keras import layers
from keras import losses

from src.definitions import ECONOMIC_DATASET_FILENAME, PROCESSED_DATA_FOLDER

def train_model():
    dataset = pd.read_csv(PROCESSED_DATA_FOLDER / ECONOMIC_DATASET_FILENAME)
    columns_count = len(dataset.columns)
    x, y = dataset.iloc[:-columns_count], dataset.iloc[-columns_count:]

    model = keras.Sequential(
        layers=[
            layers.Input(shape=(5,), name="input"),
            layers.Dense(10, name="inner"),
            layers.Dense(1, name="output")
        ]
    )    

    opt = tfp.optimizer.differential_evolution_minimize(
        losses.mean_squared_error,
        initial_population=40,
        initial_position=None,
        population_size=50,
        population_stddev=1.0,
        max_iterations=1000,
        func_tolerance=0,
        position_tolerance=1e-08,
        differential_weight=0.5,
        crossover_prob=0.9,
        seed=None,
        name=None,
    )

    model.compile(
        optimizer=opt,
        loss=losses.mean_squared_error,
        metrics=["accuracy"],
    )

    model.fit(x, y, epochs=1000)
