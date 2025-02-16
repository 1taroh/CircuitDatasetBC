from pathlib import Path
import os
import pandas as pd

# 検索関数
def search(df, **kwargs):
    '''
    >>> result = search(df, p_L=0.)
    >>> print(result['path_raw'])
###########################################
    >>> result = search(
        dataset_df,
        boundary_type="match",
        graph_type="Comet",
        p_G_load=0.1,
        p_L=0.0,
        p_C=0.0,
        missing_values=5,
    )
    # !NOTE 発行されたクエリで複数の結果が返ってきたときには先頭を取得する
    >>> raw_data = Path(result["path_raw"].iloc[0])
    >>> processed_data = Path(result["path_processed"].iloc[0])
    '''
    query_parts = []
    for key, value in kwargs.items():
        # 文字列型はシングルクォート"'"を追加
        if isinstance(value, str):
            query_parts.append(f"{key} == '{value}'")
        else:
            query_parts.append(f"{key} == {value}")
    query = " & ".join(query_parts)
    print(f'query: {query}')
    result = df.query(query)
    return result if not result.empty else None

data = [
        {
        'path_raw'       : Path('../data/path/nodal_potential_2024-11-22_1.csv'),
        'path_processed' : Path('../data/processed/path/processed_nodal_potential_2024-11-22_1.csv'),
        'graph_type'     : 'Path',
        'boundary_type'  : 'match',
        'p_G_load'       : 0.1,
        'p_L'            : 0.,
        'p_C'            : 0.,
        'missing_values' : 5,
    },
    {
        'path_raw'       :  Path('../data/path/nodal_potential_2024-11-22_1.csv'),
        'path_processed' :  Path('../data/path/processed/processed_nodal_potential_2024-11-22_1_num=10.csv'),
        'graph_type'     : 'Path',
        'boundary_type'  : 'match',
        'p_G_load'       : 0.1,
        'p_L'            : 0.,
        'p_C'            : 0.,
        'missing_values' : 10,
    },
    {
        'path_raw'       : Path('../data/branch/nodal_potential_2024-12-04_1.csv'),
        'path_processed' : Path('../data/processed/branch/processed_nodal_potential_2024-12-04_1.csv'),
        'graph_type'     : 'Branch',
        'boundary_type'  : 'match',
        'p_G_load'       : 0.1,
        'p_L'            : 0.,
        'p_C'            : 0.,
        'missing_values' : 5,
    },
    {
        'path_raw'       : Path('../data/branch/nodal_potential_2024-12-04_1.csv'),
        'path_processed' : Path('../data/processed/branch/processed_nodal_potential_2024-12-04_1_num=10.csv'),
        'graph_type'     : 'Branch',
        'boundary_type'  : 'match',
        'p_G_load'       : 0.1,
        'p_L'            : 0.,
        'p_C'            : 0.,
        'missing_values' : 10,
    },
    {
        'path_raw'       :Path('../data/comet/nodal_potential_2024-11-23_1.csv'),
        'path_processed' :Path('../data/processed/comet/processed_nodal_potential_2024-11-23_1_num=5.csv'),
        'graph_type'     : 'Comet',
        'boundary_type'  : 'match',
        'p_G_load'       : 0.1,
        'p_L'            : 0.,
        'p_C'            : 0.,
        'missing_values' : 5,
    },
    {
        'path_raw'       :Path('../data/comet/nodal_potential_2024-11-23_1.csv'),
        'path_processed' :Path('../data/processed/comet/processed_nodal_potential_2024-11-23_1_num=10.csv'),
        'graph_type'     : 'Comet',
        'boundary_type'  : 'match',
        'p_G_load'       : 0.1,
        'p_L'            : 0.,
        'p_C'            : 0.,
        'missing_values' : 10,
    },
    {
        'path_raw'       : Path('../data/erdos_renyi/nodal_potential_2024-11-26_1.csv'),
        'path_processed' : Path('../data/processed/erdos_renyi/processed_nodal_potential_2024-11-26_1_num=5.csv'),
        'graph_type'     : 'Erdos-Renyi',
        'boundary_type'  : 'match',
        'p_G_load'       : 0.1,
        'p_L'            : 0.,
        'p_C'            : 0.,
        'missing_values' : 5,
    },
    {
        'path_raw'       : Path('../data/erdos_renyi/nodal_potential_2024-11-26_1.csv'),
        'path_processed' : Path('../data/processed/erdos_renyi/processed_nodal_potential_2024-11-26_1_num=10.csv'),
        'graph_type'     : 'Erdos-Renyi',
        'boundary_type'  : 'match',
        'p_G_load'       : 0.1,
        'p_L'            : 0.,
        'p_C'            : 0.,
        'missing_values' : 10,
    },
]

dataset_df = pd.DataFrame(data)
__all__ = [dataset_df]
