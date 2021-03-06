PGDMP                         z         	   db_tg_bot    14.2    14.2 .               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16394 	   db_tg_bot    DATABASE     j   CREATE DATABASE db_tg_bot WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Kazakhstan.1251';
    DROP DATABASE db_tg_bot;
                postgres    false                       0    0    DATABASE db_tg_bot    ACL     ?   REVOKE CONNECT,TEMPORARY ON DATABASE db_tg_bot FROM PUBLIC;
GRANT CONNECT ON DATABASE db_tg_bot TO tg_bot_select_insert;
GRANT CONNECT ON DATABASE db_tg_bot TO power_bi_user;
                   postgres    false    3354                        2615    16404    tg_bot_database    SCHEMA        CREATE SCHEMA tg_bot_database;
    DROP SCHEMA tg_bot_database;
                postgres    false                       0    0    SCHEMA tg_bot_database    ACL     :   GRANT USAGE ON SCHEMA tg_bot_database TO tg_bot_raw_user;
                   postgres    false    6            ?            1259    16419    customer_numbers    TABLE     ?  CREATE TABLE tg_bot_database.customer_numbers (
    id integer NOT NULL,
    customer_number character varying(11) NOT NULL,
    office character varying(55) NOT NULL,
    date date NOT NULL,
    user_fullname character varying(32) NOT NULL,
    is_superapp_user boolean DEFAULT false NOT NULL,
    is_seen_in_last_90_days boolean DEFAULT false NOT NULL,
    city character varying(20) NOT NULL
);
 -   DROP TABLE tg_bot_database.customer_numbers;
       tg_bot_database         heap    postgres    false    6                       0    0    TABLE customer_numbers    ACL     ?  GRANT SELECT,INSERT,UPDATE ON TABLE tg_bot_database.customer_numbers TO tg_bot WITH GRANT OPTION;
GRANT SELECT,INSERT ON TABLE tg_bot_database.customer_numbers TO tg_bot_read_insert;
GRANT SELECT,INSERT,UPDATE ON TABLE tg_bot_database.customer_numbers TO tg_bot_select_insert;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE tg_bot_database.customer_numbers TO tg_bot_raw_user;
GRANT SELECT ON TABLE tg_bot_database.customer_numbers TO power_bi_user;
          tg_bot_database          postgres    false    213            ?            1259    16418    customer_numbers_id_seq    SEQUENCE     ?   CREATE SEQUENCE tg_bot_database.customer_numbers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE tg_bot_database.customer_numbers_id_seq;
       tg_bot_database          postgres    false    213    6                       0    0    customer_numbers_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE tg_bot_database.customer_numbers_id_seq OWNED BY tg_bot_database.customer_numbers.id;
          tg_bot_database          postgres    false    212                       0    0     SEQUENCE customer_numbers_id_seq    ACL     ?   GRANT SELECT ON SEQUENCE tg_bot_database.customer_numbers_id_seq TO tg_bot_read_insert;
GRANT ALL ON SEQUENCE tg_bot_database.customer_numbers_id_seq TO tg_bot_raw_user;
GRANT SELECT ON SEQUENCE tg_bot_database.customer_numbers_id_seq TO power_bi_user;
          tg_bot_database          postgres    false    212            ?            1259    16480    messages_from_users    TABLE     ?   CREATE TABLE tg_bot_database.messages_from_users (
    id integer NOT NULL,
    date timestamp without time zone NOT NULL,
    username character varying(32) NOT NULL,
    text text NOT NULL
);
 0   DROP TABLE tg_bot_database.messages_from_users;
       tg_bot_database         heap    postgres    false    6                        0    0    TABLE messages_from_users    ACL     ?   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE tg_bot_database.messages_from_users TO tg_bot_raw_user;
GRANT SELECT ON TABLE tg_bot_database.messages_from_users TO power_bi_user;
          tg_bot_database          postgres    false    217            ?            1259    16479    messages_from_users_id_seq    SEQUENCE     ?   CREATE SEQUENCE tg_bot_database.messages_from_users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE tg_bot_database.messages_from_users_id_seq;
       tg_bot_database          postgres    false    6    217            !           0    0    messages_from_users_id_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE tg_bot_database.messages_from_users_id_seq OWNED BY tg_bot_database.messages_from_users.id;
          tg_bot_database          postgres    false    216            "           0    0 #   SEQUENCE messages_from_users_id_seq    ACL     ?   GRANT ALL ON SEQUENCE tg_bot_database.messages_from_users_id_seq TO tg_bot_raw_user;
GRANT SELECT ON SEQUENCE tg_bot_database.messages_from_users_id_seq TO power_bi_user;
          tg_bot_database          postgres    false    216            ?            1259    16473    stores    TABLE     ?   CREATE TABLE tg_bot_database.stores (
    id integer NOT NULL,
    city character varying(25) NOT NULL,
    store character varying(55) NOT NULL
);
 #   DROP TABLE tg_bot_database.stores;
       tg_bot_database         heap    postgres    false    6            #           0    0    TABLE stores    ACL     ?   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE tg_bot_database.stores TO tg_bot_raw_user;
GRANT SELECT ON TABLE tg_bot_database.stores TO power_bi_user;
          tg_bot_database          postgres    false    215            ?            1259    16472    stores_id_seq    SEQUENCE     ?   CREATE SEQUENCE tg_bot_database.stores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE tg_bot_database.stores_id_seq;
       tg_bot_database          postgres    false    215    6            $           0    0    stores_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE tg_bot_database.stores_id_seq OWNED BY tg_bot_database.stores.id;
          tg_bot_database          postgres    false    214            %           0    0    SEQUENCE stores_id_seq    ACL     ?   GRANT ALL ON SEQUENCE tg_bot_database.stores_id_seq TO tg_bot_raw_user;
GRANT SELECT ON SEQUENCE tg_bot_database.stores_id_seq TO power_bi_user;
          tg_bot_database          postgres    false    214            ?            1259    16409    users    TABLE     ?  CREATE TABLE tg_bot_database.users (
    id integer NOT NULL,
    username_tg character varying(32) NOT NULL,
    full_name character varying(32) NOT NULL,
    office character varying(55) NOT NULL,
    rights character varying(12) NOT NULL,
    city character varying(20) NOT NULL,
    tg_user_id character varying(32) DEFAULT 'not set'::character varying NOT NULL,
    tg_chat_id character varying(32) DEFAULT 'not set'::character varying NOT NULL
);
 "   DROP TABLE tg_bot_database.users;
       tg_bot_database         heap    postgres    false    6            &           0    0    TABLE users    ACL     ?  GRANT SELECT,INSERT,UPDATE ON TABLE tg_bot_database.users TO tg_bot WITH GRANT OPTION;
GRANT SELECT,INSERT ON TABLE tg_bot_database.users TO tg_bot_read_insert;
GRANT SELECT,INSERT,UPDATE ON TABLE tg_bot_database.users TO tg_bot_select_insert;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE tg_bot_database.users TO tg_bot_raw_user;
GRANT SELECT ON TABLE tg_bot_database.users TO power_bi_user;
          tg_bot_database          postgres    false    211            ?            1259    16408    users_id_seq    SEQUENCE     ?   CREATE SEQUENCE tg_bot_database.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE tg_bot_database.users_id_seq;
       tg_bot_database          postgres    false    6    211            '           0    0    users_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE tg_bot_database.users_id_seq OWNED BY tg_bot_database.users.id;
          tg_bot_database          postgres    false    210            (           0    0    SEQUENCE users_id_seq    ACL     ?   GRANT SELECT ON SEQUENCE tg_bot_database.users_id_seq TO tg_bot_read_insert;
GRANT ALL ON SEQUENCE tg_bot_database.users_id_seq TO tg_bot_raw_user;
GRANT SELECT ON SEQUENCE tg_bot_database.users_id_seq TO power_bi_user;
          tg_bot_database          postgres    false    210            o           2604    16422    customer_numbers id    DEFAULT     ?   ALTER TABLE ONLY tg_bot_database.customer_numbers ALTER COLUMN id SET DEFAULT nextval('tg_bot_database.customer_numbers_id_seq'::regclass);
 K   ALTER TABLE tg_bot_database.customer_numbers ALTER COLUMN id DROP DEFAULT;
       tg_bot_database          postgres    false    212    213    213            s           2604    16483    messages_from_users id    DEFAULT     ?   ALTER TABLE ONLY tg_bot_database.messages_from_users ALTER COLUMN id SET DEFAULT nextval('tg_bot_database.messages_from_users_id_seq'::regclass);
 N   ALTER TABLE tg_bot_database.messages_from_users ALTER COLUMN id DROP DEFAULT;
       tg_bot_database          postgres    false    217    216    217            r           2604    16476 	   stores id    DEFAULT     x   ALTER TABLE ONLY tg_bot_database.stores ALTER COLUMN id SET DEFAULT nextval('tg_bot_database.stores_id_seq'::regclass);
 A   ALTER TABLE tg_bot_database.stores ALTER COLUMN id DROP DEFAULT;
       tg_bot_database          postgres    false    215    214    215            l           2604    16412    users id    DEFAULT     v   ALTER TABLE ONLY tg_bot_database.users ALTER COLUMN id SET DEFAULT nextval('tg_bot_database.users_id_seq'::regclass);
 @   ALTER TABLE tg_bot_database.users ALTER COLUMN id DROP DEFAULT;
       tg_bot_database          postgres    false    211    210    211                      0    16419    customer_numbers 
   TABLE DATA           ?   COPY tg_bot_database.customer_numbers (id, customer_number, office, date, user_fullname, is_superapp_user, is_seen_in_last_90_days, city) FROM stdin;
    tg_bot_database          postgres    false    213   ?:                 0    16480    messages_from_users 
   TABLE DATA           P   COPY tg_bot_database.messages_from_users (id, date, username, text) FROM stdin;
    tg_bot_database          postgres    false    217   ?:                 0    16473    stores 
   TABLE DATA           :   COPY tg_bot_database.stores (id, city, store) FROM stdin;
    tg_bot_database          postgres    false    215   ?:                 0    16409    users 
   TABLE DATA           r   COPY tg_bot_database.users (id, username_tg, full_name, office, rights, city, tg_user_id, tg_chat_id) FROM stdin;
    tg_bot_database          postgres    false    211   8=       )           0    0    customer_numbers_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('tg_bot_database.customer_numbers_id_seq', 39, true);
          tg_bot_database          postgres    false    212            *           0    0    messages_from_users_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('tg_bot_database.messages_from_users_id_seq', 646, true);
          tg_bot_database          postgres    false    216            +           0    0    stores_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('tg_bot_database.stores_id_seq', 44, true);
          tg_bot_database          postgres    false    214            ,           0    0    users_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('tg_bot_database.users_id_seq', 48, true);
          tg_bot_database          postgres    false    210            }           2606    16490    stores city_store 
   CONSTRAINT     \   ALTER TABLE ONLY tg_bot_database.stores
    ADD CONSTRAINT city_store UNIQUE (city, store);
 D   ALTER TABLE ONLY tg_bot_database.stores DROP CONSTRAINT city_store;
       tg_bot_database            postgres    false    215    215            y           2606    16426 &   customer_numbers customer_numbers_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY tg_bot_database.customer_numbers
    ADD CONSTRAINT customer_numbers_pkey PRIMARY KEY (id);
 Y   ALTER TABLE ONLY tg_bot_database.customer_numbers DROP CONSTRAINT customer_numbers_pkey;
       tg_bot_database            postgres    false    213            ?           2606    16487 ,   messages_from_users messages_from_users_pkey 
   CONSTRAINT     s   ALTER TABLE ONLY tg_bot_database.messages_from_users
    ADD CONSTRAINT messages_from_users_pkey PRIMARY KEY (id);
 _   ALTER TABLE ONLY tg_bot_database.messages_from_users DROP CONSTRAINT messages_from_users_pkey;
       tg_bot_database            postgres    false    217                       2606    16478    stores stores_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY tg_bot_database.stores
    ADD CONSTRAINT stores_pkey PRIMARY KEY (id);
 E   ALTER TABLE ONLY tg_bot_database.stores DROP CONSTRAINT stores_pkey;
       tg_bot_database            postgres    false    215            {           2606    24640    customer_numbers unique_number 
   CONSTRAINT     s   ALTER TABLE ONLY tg_bot_database.customer_numbers
    ADD CONSTRAINT unique_number UNIQUE (customer_number, date);
 Q   ALTER TABLE ONLY tg_bot_database.customer_numbers DROP CONSTRAINT unique_number;
       tg_bot_database            postgres    false    213    213            u           2606    16498    users unique_user 
   CONSTRAINT     h   ALTER TABLE ONLY tg_bot_database.users
    ADD CONSTRAINT unique_user UNIQUE (full_name, office, city);
 D   ALTER TABLE ONLY tg_bot_database.users DROP CONSTRAINT unique_user;
       tg_bot_database            postgres    false    211    211    211            w           2606    16416    users users_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY tg_bot_database.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 C   ALTER TABLE ONLY tg_bot_database.users DROP CONSTRAINT users_pkey;
       tg_bot_database            postgres    false    211                  x?????? ? ?            x?????? ? ?         ?  x????o?@?g?O?/Ъ?!!c?JJT?Ru??X>s?l????R:t????.i???+?}??gL??t`{?{?%?I=葚?q?vJ???μSZ?~D??l??????????1??j?i?l????j?w??Ev???C?| ?"?A?`?i֒>m҅?<p???Ed?	cP?M??a$}똑???n?5os???D??l? H?b?$??n????$??M???<????.?Ai	)??V???J??T-??ޡ?c????18J?%'??$so???????????^$???aW?H?4w#k?;?l?}????pI??[laf	*??j??9???d\``?|?c=|???X??󳽆?d??p??~C?^??y>Nw?T???g N?I???????p*O???JZ-~???M/????}?4@???Y??<S?f?c2`?E0Cՠ?;^?_ݚ???h$xϜ?>8??:????\?x?.?l?????nL??6?Q?5?f_??|6???[2b????z+?4.Z??۲H?Y?Q6QG>?F????G7W??Gf?N?+b7X????9 ??g??            x?????? ? ?     