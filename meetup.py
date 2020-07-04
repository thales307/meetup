import calendar
import datetime


def meetup(year, month, week, day_of_week):
    cal = calendar.Calendar()
    week_days = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_of_week_num = week_days.index(day_of_week)
    candidates = [day for day, dow in list(cal.itermonthdays2(
        year, month)) if dow == day_of_week_num and day > 0]

    if week == 'teenth':
        target_day = [c for c in candidates if c > 12][0]
        return datetime.date(year, month, target_day)
    elif week == 'last':
        candidates2 = [c for c in candidates if c > 12]
        target_day = candidates2[len(candidates2) - 1]
        return datetime.date(year, month, target_day)
    else:
        try:
            week_num = int(week[0]) - 1
            target_day = candidates[week_num]
            return datetime.date(year, month, target_day)
        except Exception:
            raise MeetupDayException('Wrong date.')


class MeetupDayException(Exception):
    pass
