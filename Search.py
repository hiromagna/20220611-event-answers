def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    start = 0   #探索範囲の開始地点 はじめはindex0
    end = len(sorted_array) - 1  #探索範囲の終点  はじめは配列の最後のindex
    mid = 0   #探索範囲の真ん中  実際に探索対象と比較するindex 初期化としてとりあえず0を入れた
    while(start <= end):    #もしstart>endなら探索範囲がなくなったのでwhile文を終了
        mid = (start + end) // 2    #探索範囲の真ん中を求める
        if(target_number == sorted_array[mid]):
            return mid
        elif(target_number < sorted_array[mid]):
            end = mid - 1 #探索範囲をstartからmid-1に絞れた
        else:
            start = mid + 1  #探索範囲をmid+1からendに絞れた
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
