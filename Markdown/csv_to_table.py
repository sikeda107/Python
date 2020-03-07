import csv

def exec():
  print('読み込むファイル名を入力してください:')
  file_name = input()

  if not file_name:
      print('test.csvを設定します:')
      file_name = './test.csv'

  print(file_name,'を開きます')
  csv_file = open(file_name, "r",
                  encoding="utf8", errors="", newline="")
  # リスト形式
  print('CSVファイルを読み込みます:', file_name)
  f = csv.reader(csv_file, delimiter=",", doublequote=True,
                lineterminator="\r\n", quotechar='"', skipinitialspace=True)

  header = next(f)
  print('ヘッダーを表示します')
  print(header)

  print('データを表示します')
  data = []
  for row in f:
    print(row)
    data.append(row)

  output_table(header,data,file_name)

def output_table(header, data, file_name):
  # Markdownテーブルの記号をリストへ追加する
  header_markdown = get_markdown_table_format(header)
  separator_markdown = get_markdown_table_sepalator(len(header), 'left')
  data_markdown = []
  for d in data:
    data_markdown.append(get_markdown_table_format(d))
  # Markdownファイルに出力する
  output_file_name = file_name.replace('.csv', '.md')
  print(output_file_name, 'に出力開始')
  with open(output_file_name, mode='w') as f:
    for h in header_markdown:
      f.write(h)
    f.write('\n')
    for s in separator_markdown:
      f.write(s)
    f.write('\n')
    for row in data_markdown:
      for cell in row:
        f.write(cell)
      f.write('\n')
  print('[完了]')
  print('出力ファイルを読み込みます')
  with open(output_file_name) as f:
    print(f.read())
  print('[完了]')

def get_markdown_table_format(data):
  data_markdown = ['| ']
  for d in data:
    data_markdown.append(d)
    data_markdown.append(' | ')
  return data_markdown

def get_markdown_table_sepalator(size, align):
  # 指定がない場合は中央寄せ
  if align is 'right':
    align_markdown = '---:'
  elif align is 'left':
    align_markdown = ':---'
  else :
    align_markdown = ':---:'

  separator_markdown = ['| ']
  for r in range(size):
    separator_markdown.append(align_markdown + '| ')
  return separator_markdown

if __name__ == '__main__':
    exec()
