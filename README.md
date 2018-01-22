# ADRs_Extract(f不良反应抽取)

To  see how the system work, just look at the `Method.bmp` ,that's a workflow of our system.

## INPUT　DATA 

- In the `input/` folder, we need an `articles.csv` file to save the users' text what you collected from the web. It's content like this:

  ```
  100001, Good morning Deepdive. I hate you.
  100002, Oh you break my heart!
  ...
  ```

  The first part is the **ID** of articles, follow by a  comma.

  The Second part is the content of article which should not have any comma (*because csv use comma to separate the different part in `.csv`* )

- In the `input/` folder, we need an `ards_dbdata.csv` file to save the known ADRs of specific **Medicine**. It's content like this:

  ```
  优甲乐,头晕
  优甲乐,胃痛
  ...
  ```

  The first part is the **Name** of target Medicine. The second part is the ARDs of that Medicine.

- In the `udf/reco_med_ard_guo.py`, the function need a list parameter which contain every ADR of all Medicine we know. It is like this:

  ```python
  list ards=['血压升高','头晕',........]  #in python language
  ```

   

