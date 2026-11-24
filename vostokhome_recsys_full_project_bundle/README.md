# Архитектура интернет-магазина «Восток-Техно & Дом» с рекомендательной системой

## О проекте
Учебный архитектурный проект масштабного интернет-магазина бытовой электроники и товаров для дома, в котором каталог, поведение посетителей, сегментация и гибридный рекомендательный движок объединены в единую информационную систему.

## Состав материалов репозитория
- `docs/VostokHome_RecSys_Full_Report.docx` — полный отчёт в формате Word со всеми 15 разделами, формулами, обоснованиями коэффициентов, схемами архитектуры/БД, диаграммами последовательности, спецификацией экранов и таблицей тестирования.
- `docs/figma_prototype_spec.md` — подробная карта 12 экранов, состояний и интерактивных переходов для сборки прототипа в Figma.
- `data/vostokhome_recsys_project_data.xlsx` — электронная таблица (14 листов):
  - `01_Categories_24Subs` — дерево из 8 категорий и 24 подкатегорий;
  - `02_Products_200` — реестр 200 товаров (`PRD-001`..`PRD-200`) с ценами, скидками, остатками и характеристиками;
  - `03_Buyers_10`, `04_Groups_5`, `05_Events_140` — 10 вымышленных покупателей, 5 групп потребления и 140 событий в 34 сеансах;
  - `06_UserPref_Before` .. `13_ItemPref_200x12` — все 5 матриц (включая состояния «до» и «после»);
  - `14_RecSys_Calc` — расчёт и сравнение гибридного ранжирования для 8 кандидатов.
- `scripts/recsys_simulation.py` — воспроизводимый Python-скрипт расчёта матриц, пересчёта предпочтений и ранжирования рекомендаций.
- `prototype/index.html` — интерактивный кликабельный прототип интерфейса (12 экранов, смена ролей Гость / USR-01 / USR-03, мобильный режим, управление предпочтениями и корзина) для демонстрации и переноса в Figma (`html.to.design`).

## Порядок просмотра
1. Открыть `docs/VostokHome_RecSys_Full_Report.docx` для изучения архитектурных решений, формул и обоснований.
2. Открыть `data/vostokhome_recsys_project_data.xlsx` для проверки полных таблиц каталога (200 SKU), журнала событий (140 записей) и пяти матриц.
3. Открыть `prototype/index.html` в браузере (или импортировать в Figma через плагин `html.to.design`) для демонстрации пользовательских сценариев.
4. Запустить `python scripts/recsys_simulation.py` для воспроизведения числовых расчётов.

## План коммитов при загрузке в GitHub
1. `feat(catalog): add 8 categories, 24 subcategories and 200 SKU registry`
2. `feat(users): add 10 fictional buyers, 5 consumption groups and 140 session events`
3. `feat(matrices): compute user-pref, group-pref, group-cat and item-pref matrices`
4. `feat(recsys): implement sparse item-item graph (225 links) and hybrid ranking simulation`
5. `docs(architecture-ui): add full Word report, interactive prototype and README`
