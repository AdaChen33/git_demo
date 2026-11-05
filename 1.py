# 学生成绩管理程序

students = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 96
}

# 显示所有学生成绩
print("===== 学生成绩管理系统 =====")

for name, score in students.items():
    print(f"学生：{name}，成绩：{score}")

# 计算平均成绩
average = sum(students.values()) / len(students)
print(f"\n平均成绩：{average:.2f}")

# 查找最高分
best_student = max(students, key=students.get)
print(f"最高分学生：{best_student}")
print(f"最高成绩：{students[best_student]}")

# 添加一名学生
students["小明"] = 88

print("\n添加学生后：")
print(students)