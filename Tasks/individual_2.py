#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import json
import os
import sys
from dotenv import load_dotenv


@click.group()
def cli():
    pass


@cli.command()
@click.argument('data')
@click.option("-n", "--name")
@click.option("-g", "--group")
@click.option("-p", "--progress")
def add(data, name, group, progress):
    """
    Добавление нового студента
    """
    if os.path.exists(data):
        load_dotenv()
        dotenv_path = os.getenv("STUDENTS_DATA")
        if not dotenv_path:
            click.secho('Файла нет', fg='red')
            sys.exit(1)
        if os.path.exists(dotenv_path):
            students = open_file(dotenv_path)
        else:
            students = []
        students.append(
            {
                'name': name,
                'group': group,
                'progress': progress
            }
        )
        with open(dotenv_path, "w", encoding="utf-8") as out:
            json.dump(students, out, ensure_ascii=False, indent=4)
        click.secho("Студент добавлен", fg='green')
    else:
        click.secho('Файла нет', fg='red')


@cli.command()
@click.argument('filename')
def select(filename):
    """
    Выбор студента по успеваемости
    """
    if os.path.exists(filename):
        load_dotenv()
        dotenv_path = os.getenv("STUDENTS_DATA")
        if not dotenv_path:
            click.secho('Файла нет', fg='red')
            sys.exit(1)
        if os.path.exists(dotenv_path):
            students = open(dotenv_path)
        else:
            students = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Ф.И.О.",
                "Группа",
                "Успеваемость"
            )
        )
        print(line)
        for pupil in students:
            evaluations = pupil.get('progress', '')
            list_of_rating = list(evaluations)
            count = 0
            for z in list_of_rating:
                if z == '2':
                    count += 1
                    print(
                        '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                            count,
                            pupil.get('name', ''),
                            pupil.get('group', ''),
                            pupil.get('progress', 0)
                        )
                    )
        print(line)


@cli.command()
@click.argument('filename')
def display(filename):
    """
    Вывод списка студентов
    """
    if os.path.exists(filename):
        load_dotenv()
        dotenv_path = os.getenv("STUDENTS_DATA")
        if not dotenv_path:
            click.secho('Файла нет', fg='red')
            sys.exit(1)
        if os.path.exists(dotenv_path):
            students = open_file(dotenv_path)
        else:
            students = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Ф.И.О.",
                "Группа",
                "Успеваемость"
            )
        )
        print(line)
        for i, pupul in enumerate(students, 1):
            print(
                '| {:<4} | {:<30} | {:<20} | {:<15} |'.format(
                    i,
                    pupul.get('name', ''),
                    pupul.get('group', ''),
                    pupul.get('progress', 0)
                )
            )
        print(line)


def open_file(filename):
    with open(filename, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    cli()


if __name__ == '__main__':
    main()
