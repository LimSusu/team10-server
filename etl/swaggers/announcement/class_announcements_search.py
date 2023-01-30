from drf_yasg.openapi import *

class_announcements_search_operation_description = "기능\n" \
                                                   "- 특정 수업의 공지사항 검색 기능을 지원합니다.\n" \
                                                   "- URL의 {id}에는 특정 수업의 id가 들어갑니다.\n" \
                                                   "- 특정 수업의 공지사항 \"제목\"을 검색합니다.\n" \
                                                   "- 페이지네이션이 적용되어, 생성 시간 역순(최근순)으로 공지사항을 " \
                                                   "10개씩 반환합니다.\n" \
                                                   "\npermission\n" \
                                                   "- admin 계정\n" \
                                                   "- 로그인 && 개인정보 세팅 완료\n" \
                                                   "\nrequest body\n" \
                                                   "- 아무것도 없습니다.\n" \
                                                   "\nparameters\n" \
                                                   "- name(필수)\n" \
                                                   "\nresponses\n" \
                                                   "- 200: 공지사항 검색 성공\n" \
                                                   "\n사용 예시\n" \
                                                   "- id=1인 수업에서 '성적' 키워드가 들어간 공지글 목록의 3번째 페이지를 불러오고 싶을 때, " \
                                                   "'baseURL/etl/class/1/announcements/search/?name=성적&page=3' GET 요청"

class_announcements_search_responses = {
    200: Schema(
        'Announcement Search Result',
        type=TYPE_OBJECT,
        properties={
            'next': Schema(
                type=TYPE_STRING,
                description='다음 10개의 공지사항을 불러올 API 주소를 담고 있습니다.\n'
                            '만약 현재 불러온 공지사항들이 마지막이라면, null 값을 갖습니다.',
            ),
            'previous': Schema(
                type=TYPE_STRING,
                description='이전 10개의 공지사항을 불러올 API 주소를 담고 있습니다.\n'
                            '처음 공지사항을 불러왔을 때는, 이전 10개의 공지사항이 없으므로 null 값을 갖습니다.',
            ),
            'results': Schema(
                type=TYPE_ARRAY,
                description='공지사항 검색 결과로 반환되는 리스트입니다.',
                items=Schema(
                    'Announcement',
                    type=TYPE_OBJECT,
                    properties={
                        'id': Schema(
                            type=TYPE_INTEGER,
                            read_only=True,
                        ),
                        'title': Schema(
                            type=TYPE_STRING,
                            description='공지사항 제목입니다.',
                        ),
                        'content': Schema(
                            type=TYPE_STRING,
                            description='공지글 내용입니다. 내용이 10글자를 넘어간다면, 10글자까지 자르고 뒤에 "..."을 붙여 반환합니다.',
                        ),
                        'created_by': Schema(
                            type=TYPE_OBJECT,
                            description='공지 작성자 정보입니다.\n',
                            properties={
                                'id': Schema(
                                    type=TYPE_INTEGER,
                                    read_only=True,
                                ),
                                'username': Schema(
                                    type=TYPE_STRING,
                                ),
                                'student_id': Schema(
                                    type=TYPE_STRING,
                                ),
                                'is_professor': Schema(
                                    type=TYPE_BOOLEAN,
                                ),
                            },
                        ),
                        'created_at': Schema(
                            type=TYPE_STRING,
                            description='공지글 생성 시간입니다. 13자리 timestamp 형식입니다.'
                        ),
                        'comment_count': Schema(
                            type=TYPE_INTEGER,
                            description='해당 공지글에 달린 댓글 수입니다.'
                        ),
                        'hits': Schema(
                            type=TYPE_INTEGER,
                            description='해당 공지글의 조회수입니다.\n"baseURL/etl/announcement/{id}/"에 GET 요청을 '
                                        '넣을 때마다, 조회수는 1씩 증가합니다.'
                        ),
                    }
                )
            ),
            'total_announcemnt_count': Schema(
                type=TYPE_INTEGER,
                description='검색 조건을 만족하는 공지글의 갯수입니다.'
            )
        }
    ),
}

class_announcements_search_parameter_name = Parameter(
    'name',
    IN_QUERY,
    description='해당 name을 포함한 제목을 가지고 있는 공지사항을 불러옵니다.',
    required=True,
    type=TYPE_STRING,
)

class_announcements_search_parameter_page = Parameter(
    'page',
    IN_QUERY,
    description='페이지네이션을 통해 해당하는 페이지를 불러옵니다.',
    required=True,
    type=TYPE_STRING,
)

class_announcements_search_manual_parameters = [
    class_announcements_search_parameter_name,
    class_announcements_search_parameter_page,
]
