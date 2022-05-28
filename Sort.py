def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    divide = 0 #配列を左から検索して基準値未満とそれ以外に左右で分けるindexの値
    right = len(array)-1 #配列を右から検索 配列最後のindexで初期化
    while(divide <= right): #左からの検索と右からの検索が交差するまでループ
        while(array[divide] < pivot): #基準値以上を見つけるまで左検索続行
            divide += 1
        while(array[right] >= pivot): #基準値未満を見つけるまで右検索続行
            right -= 1
            if(right<0): #配列が全て昇順に並んでいた場合rightが負の値をとるのでその例外を処理
                return array
        if (divide < right):    #配列のdivide未満のindexに基準値未満の値、それ以上のindexに基準値以上の値を格納する
            array[divide], array[right] = array[right], array[divide] #配列の値を入れ替える
            divide += 1     #divideとrightの検索位置を1つずつ進める
            right -= 1
        else:
            break
    if(len(array[:divide]) >= 2): #配列の要素数が1以上でないと下の処理でエラー
        array[:divide] = sort(array[:divide]) #配列の範囲index0からdivide-1までで再帰
    if(len(array[divide:]) >= 2): #配列の要素数が1以上でないと下の処理でエラー
        array[divide:] = sort(array[divide:]) #配列の範囲index divide+1から配列の最後で再帰
    #array = array[:divide] + array[divide:]
    return array
    # ここまで記述

if __name__ == '__main__':
    main()