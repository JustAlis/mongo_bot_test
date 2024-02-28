import json
import pandas as pd

def parse_input(input: str):
    data = json.loads(input)
    return (data["group_type"], data["dt_from"], data["dt_upto"])


def fill_missing_values(dataset:list, 
                        labels:list, 
                        dt_from:str, 
                        dt_upto:str,
                        aggregation_type: str):

    if aggregation_type == "day":
        freq = "D"
    elif aggregation_type == "hour":
        freq = "h"
    elif aggregation_type == "month":
        freq = "MS"
    else:
        raise ValueError("Неподдерживаемый тип агрегации")
    
    # Преобразуем метки времени в формат datetime и установим их в качестве индекса DataFrame
    df = pd.DataFrame({"value": dataset}, dtype=int, index=pd.to_datetime(labels))
    # Создаем новый DataFrame с полным временным рядом в заданном диапазоне и присваиваем его индексу
    full_index = pd.date_range(start=pd.to_datetime(dt_from), end=pd.to_datetime(dt_upto), freq=freq)
    new_df = pd.DataFrame(index=full_index)
    # Объединяем исходный DataFrame с новым DataFrame по индексу с заполнением отсутствующих значений нулями
    merged_df = new_df.merge(df, how="left", left_index=True, right_index=True)
    # Заполняем отсутствующие значения нулями
    merged_df["value"] = merged_df["value"].fillna(0)
    # Получаем итоговый dataset и labels из DataFrame
    final_dataset = merged_df["value"].astype(int).tolist()
    merged_df.index = pd.to_datetime(merged_df.index)
    # Применение метода strftime для каждого элемента индекса
    final_labels = merged_df.index.strftime("%Y-%m-%dT%H:%M:%S").tolist()

    return json.dumps({"dataset": final_dataset, "labels": final_labels})
