# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2022-12-05
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Email methods.
"""

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from reydb import rorm, DatabaseEngine

from .rbase import Base, throw
from .rdata import unique
from .ros import FileSourceBytes, read_file_bytes

__all__ = (
    'Email',
)

class DatabaseORMTableEmailSend(rorm.Table):
    """
    Database `email_send` table ORM model.
    """

    __name__ = 'email_send'
    __comment__ = 'Email send record table.'
    id: int = rorm.Field(key_auto=True, comment='ID.')
    create_time: rorm.Datetime = rorm.Field(field_default=':time', not_null=True, index_n=True, comment='Record create time.')
    from_: str = rorm.Field(name='from', not_null=True, comment='From email addresse.')
    to: list[str] = rorm.Field(rorm.types.ARRAY(rorm.types.VARCHAR(255)), not_null=True, comment='To email addresses.')
    show_from: str | None = rorm.Field(comment='Show from email addresse.')
    show_to: list[str] | None = rorm.Field(rorm.types.ARRAY(rorm.types.VARCHAR(255)), comment='Show to email addresses.')
    show_cc: list[str] | None = rorm.Field(rorm.types.ARRAY(rorm.types.VARCHAR(255)), comment='Show carbon copy email addresses.')
    title: str | None = rorm.Field(comment='Email title.')
    text: str | None = rorm.Field(rorm.types.TEXT, comment='Email text.')
    attachment: list[str] | None = rorm.Field(rorm.types.ARRAY(rorm.types.VARCHAR(255)), comment='Email attachment names.')

class Email(Base):
    """
    Email type.
    Can create database used "self.build_db" method.
    """

    def __init__(
        self,
        username: str,
        password: str,
        db_engine: DatabaseEngine | None = None,
    ) -> None:
        """
        Build instance attributes.

        Parameters
        ----------
        username : Email username.
        password : Email password.
        db_engine : Database engine, insert request record to table.
        """

        # Set attribute.
        self.username = username
        self.password = password
        self.db_engine = db_engine
        address = self.get_server_address(self.username)
        self.smtp = SMTP(*address)

        ## Build Database.
        if self.db_engine is not None:
            self.build_db()

    def get_server_address(
        self,
        email: str
    ) -> tuple[str, str]:
        """
        Get server address of email.

        Parameters
        ----------
        email : Email address.

        Returns
        -------
        Server address.
        """

        # Get.
        domain_name = email.split('@')[-1]
        host = 'smtp.' + domain_name
        port = 25

        return host, port

    def get_smtp(self) -> SMTP:
        """
        Get `SMTP` connection instance and login.

        Returns
        -------
        Instance.
        """

        # Login.
        response = self.smtp.login(self.username, self.password)
        code = response[0]
        if code != 235:
            throw(ConnectionError, response)

        return self.smtp

    def create_email(
        self,
        title: str | None,
        text: str | None,
        attachment: dict[str, bytes],
        show_from: str | None,
        show_to: list[str] | None,
        show_cc: list[str] | None
    ) -> str:
        """
        Create email content.

        Parameters
        ----------
        title : Email title.
        text : Email text.
        attachment : Email attachments dictionary.
            - `Key`: File name.
            - `Value`: File bytes data.
        show_from : Show from email address.
        show_to : Show to email addresses list.
        show_cc : Show carbon copy email addresses list.
        """

        # Parameter.
        if type(show_to) == list:
            show_to = ','.join(show_to)
        if type(show_cc) == list:
            show_cc = ','.join(show_cc)

        # Instance.
        mimes = MIMEMultipart()

        # Add.

        ## Title.
        if title is not None:
            mimes['subject'] = title
        
        ## Text.
        if text is not None:
            mime_text = MIMEText(text)
            mimes.attach(mime_text)

        ## Attachment.
        for file_name, file_bytes in attachment.items():
            mime_file = MIMEApplication(file_bytes)
            mime_file.add_header('Content-Disposition', 'attachment', filename=file_name)
            mimes.attach(mime_file)

        ## Show from.
        if show_from is not None:
            mimes['from'] = show_from

        ## Show to.
        if show_to is not None:
            mimes['to'] = show_to

        ## Show cc.
        if show_cc is not None:
            mimes['cc'] = show_cc

        # Create.
        email = mimes.as_string()

        return email

    def send_email(
        self,
        to: str | list[str],
        title: str | None = None,
        text: str | None = None,
        attachment: dict[str, FileSourceBytes] | None = None,
        cc: str | list[str] | None = None,
        show_from: str | None = None,
        show_to: str | list[str] | None = None,
        show_cc: str | list[str] | None = None
    ) -> None:
        """
        Send email.

        Parameters
        ----------
        to : To email addresses.
            - `str`: Email address, multiple comma interval.
            - `list[str]`: Email addresses list.
        title : Email title.
        text : Email text.
        attachment : Email attachments dictionary.
            - `Key`: File name.
            - `Value`: File bytes data source.
                `bytes`: File bytes data.
                `str`: File path.
                `BufferedIOBase`: File bytes IO.
        cc : Carbon copy email addresses.
            - `str`: Email address, multiple comma interval.
            - `list[str]`: Email addresses list.
        show_from : Show from email address.
            - `None`: Use attribute `self.username`.
            - `str`: Email address.
        show_to : Show to email addresses.
            - `None`: Use parameter `to`.
            - `str`: Email address, multiple comma interval.
            - `list[str]`: Email addresses list.
        show_cc : Show carbon copy email addresses.
            - `None`: Use parameter `cc`.
            - `str`: Email address, multiple comma interval.
            - `list[str]`: Email addresses list.
        """

        # Parameter.

        ## To.
        if type(to) == str:
            to = to.split(',')

        ## Cc.
        match cc:
            case None:
                cc = []
            case str():
                cc = cc.split(',')

        ## Show from.
        show_from = show_from or self.username

        ## Show to.
        show_to = show_to or to
        if type(show_to) == str:
            show_to = show_to.split(',')

        ## Show cc.
        show_cc = show_cc or cc
        if type(show_cc) == str:
            show_cc = show_cc.split(',')

        ## Attachment.
        attachment = attachment or {}
        for file_name, file_source in attachment.items():
            file_bytes = read_file_bytes(file_source)
            attachment[file_name] = file_bytes

        # Create email.
        email = self.create_email(
            title,
            text,
            attachment,
            show_from,
            show_to,
            show_cc
        )

        # Get SMTP.
        smtp = self.get_smtp()

        # Send email.
        to += cc
        to = unique(to)
        smtp.sendmail(
            self.username,
            to,
            email
        )

        # Database.
        if self.db_engine is not None:
            data = {
                'from': self.username,
                'to': tuple(to),
                'show_from': show_from,
                'show_to': tuple(show_to),
                'show_cc': tuple(show_cc),
                'title': title,
                'text': text,
                'attachment': tuple(attachment.keys())
            }
            self.db_engine.execute.insert('email_send', data)

    __call__ = send_email

    def __del__(self) -> None:
        """
        Delete instance.
        """

        # Quit.
        self.smtp.quit()

    def build_db(self) -> None:
        """
        Check and build database tables.
        """

        # Check.
        if self.db_engine is None:
            throw(ValueError, self.db_engine)

        # Parameter.

        ## Table.
        tables = [DatabaseORMTableEmailSend]

        ## View stats.
        views_stats = [
            {
                'table': 'stats_email_send',
                'items': [
                    {
                        'name': 'count',
                        'select': (
                            'SELECT COUNT(1)\n'
                            'FROM "email_send"'
                        ),
                        'comment': 'Create count.'
                    },
                    {
                        'name': 'past_day_count',
                        'select': (
                            'SELECT COUNT(1)\n'
                            'FROM "email_send"'
                            'WHERE DATE_PART(\'day\', NOW() - "create_time") = 0'
                        ),
                        'comment': 'Create count in the past day.'
                    },
                    {
                        'name': 'past_week_count',
                        'select': (
                            'SELECT COUNT(1)\n'
                            'FROM "email_send"'
                            'WHERE DATE_PART(\'day\', NOW() - "create_time") <= 6'
                        ),
                        'comment': 'Create count in the past week.'
                    },
                    {
                        'name': 'past_month_count',
                        'select': (
                            'SELECT COUNT(1)\n'
                            'FROM "email_send"'
                            'WHERE DATE_PART(\'day\', NOW() - "create_time") <= 29'
                        ),
                        'comment': 'Create count in the past month.'
                    }
                ]
            }
        ]

        # Build.
        self.db_engine.build(tables=tables, views_stats=views_stats, skip=True)
