from database import SessionLocal
from models import Task, User

db = SessionLocal()


def seed():
    ### user1
    tasks_list = [
        ['T1_0001', 'USER1 have Task1. This is so heavy.'],
        ['T1_0002', 'USER1 have Task2. This is so easy.']
    ]
    tasks = [Task(title=task[0], text=task[1]) for task in tasks_list]

    user = User(username='user_1', email='user_1_hoge@hoge.jp')
    user.tasks = tasks  # リレーションも丸ごと表現できる

    db.add(user)

    ### user2
    tasks_list = [
        ['T2_0001', 'USER2 have Task1. This is so heavy.'],
        ['T2_0002', 'USER2 have Task2. This is so easy.'],
        ['T2_0003', 'USER2 have Task2. This is normal.']
    ]
    tasks = [Task(title=task[0], text=task[1]) for task in tasks_list]

    user = User(username='user_2', email='user_2_hoge@hoge.jp')
    user.tasks = tasks  # リレーションも丸ごと表現できる

    db.add(user)

    ### user3
    user = User(username='user_3', email='user_3_hoge@hoge.jp')
    db.add(user)

    db.commit()


if __name__ == '__main__':
    BOS = '\033[92m'  # 緑色表示用
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()