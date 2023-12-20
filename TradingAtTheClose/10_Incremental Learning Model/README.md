
predictのタイミングでもmodelを更新する
is_last=Trueのmodelを、新しいデータで更新し、モデル一覧に追加する

Revelated taregtをtrainに使うと、scoureが著しく悪くなる
 => predictのstdが急増する


学習に影響があるパラメータ
   
num_folds = 5 # クロスバリデーションの分割数
stopping_rounds = 100 # early_stopping用コールバック関数
num_boost_round = 1000 # 計算回数
update_num_boost_round = 1000 # 再学習の計算回数
continuos_train_span = 3 # DATA_COUNT_IN_SAME_BUCKET * continuos_train_span が更新の頻度
continuos_dataset_span = 20 # DATA_COUNT_IN_SAME_BUCKET * continuos_dataset_span が更新対象のデータ数
# continuos_train_span < continuos_dataset_span は必須


lgb_params # lightgbmのパラメータ
