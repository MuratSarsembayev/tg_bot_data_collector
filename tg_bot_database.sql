PGDMP         2                z         	   db_tg_bot    14.2    14.2 +               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16394 	   db_tg_bot    DATABASE     j   CREATE DATABASE db_tg_bot WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Kazakhstan.1251';
    DROP DATABASE db_tg_bot;
                postgres    false                       0    0    DATABASE db_tg_bot    ACL     �   REVOKE CONNECT,TEMPORARY ON DATABASE db_tg_bot FROM PUBLIC;
GRANT CONNECT ON DATABASE db_tg_bot TO tg_bot_select_insert;
GRANT CONNECT ON DATABASE db_tg_bot TO power_bi_user;
                   postgres    false    3346                        2615    16404    tg_bot_database    SCHEMA        CREATE SCHEMA tg_bot_database;
    DROP SCHEMA tg_bot_database;
                postgres    false                       0    0    SCHEMA tg_bot_database    ACL     :   GRANT USAGE ON SCHEMA tg_bot_database TO tg_bot_raw_user;
                   postgres    false    6            �            1259    16419    customer_numbers    TABLE     �  CREATE TABLE tg_bot_database.customer_numbers (
    id integer NOT NULL,
    customer_number character varying(11) NOT NULL,
    office character varying(55) NOT NULL,
    date timestamp without time zone NOT NULL,
    user_fullname character varying(32) NOT NULL,
    is_superapp_user boolean DEFAULT false NOT NULL,
    is_seen_in_last_90_days boolean DEFAULT false NOT NULL,
    city character varying(20) NOT NULL
);
 -   DROP TABLE tg_bot_database.customer_numbers;
       tg_bot_database         heap    postgres    false    6                       0    0    TABLE customer_numbers    ACL     �  GRANT SELECT,INSERT,UPDATE ON TABLE tg_bot_database.customer_numbers TO tg_bot WITH GRANT OPTION;
GRANT SELECT,INSERT ON TABLE tg_bot_database.customer_numbers TO tg_bot_read_insert;
GRANT SELECT,INSERT,UPDATE ON TABLE tg_bot_database.customer_numbers TO tg_bot_select_insert;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE tg_bot_database.customer_numbers TO tg_bot_raw_user;
GRANT SELECT ON TABLE tg_bot_database.customer_numbers TO power_bi_user;
          tg_bot_database          postgres    false    213            �            1259    16418    customer_numbers_id_seq    SEQUENCE     �   CREATE SEQUENCE tg_bot_database.customer_numbers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE tg_bot_database.customer_numbers_id_seq;
       tg_bot_database          postgres    false    6    213                       0    0    customer_numbers_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE tg_bot_database.customer_numbers_id_seq OWNED BY tg_bot_database.customer_numbers.id;
          tg_bot_database          postgres    false    212                       0    0     SEQUENCE customer_numbers_id_seq    ACL     �   GRANT SELECT ON SEQUENCE tg_bot_database.customer_numbers_id_seq TO tg_bot_read_insert;
GRANT ALL ON SEQUENCE tg_bot_database.customer_numbers_id_seq TO tg_bot_raw_user;
GRANT SELECT ON SEQUENCE tg_bot_database.customer_numbers_id_seq TO power_bi_user;
          tg_bot_database          postgres    false    212            �            1259    16480    messages_from_users    TABLE     �   CREATE TABLE tg_bot_database.messages_from_users (
    id integer NOT NULL,
    date timestamp without time zone NOT NULL,
    username character varying(32) NOT NULL,
    text text NOT NULL
);
 0   DROP TABLE tg_bot_database.messages_from_users;
       tg_bot_database         heap    postgres    false    6                       0    0    TABLE messages_from_users    ACL     �   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE tg_bot_database.messages_from_users TO tg_bot_raw_user;
GRANT SELECT ON TABLE tg_bot_database.messages_from_users TO power_bi_user;
          tg_bot_database          postgres    false    217            �            1259    16479    messages_from_users_id_seq    SEQUENCE     �   CREATE SEQUENCE tg_bot_database.messages_from_users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE tg_bot_database.messages_from_users_id_seq;
       tg_bot_database          postgres    false    6    217                       0    0    messages_from_users_id_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE tg_bot_database.messages_from_users_id_seq OWNED BY tg_bot_database.messages_from_users.id;
          tg_bot_database          postgres    false    216                       0    0 #   SEQUENCE messages_from_users_id_seq    ACL     �   GRANT ALL ON SEQUENCE tg_bot_database.messages_from_users_id_seq TO tg_bot_raw_user;
GRANT SELECT ON SEQUENCE tg_bot_database.messages_from_users_id_seq TO power_bi_user;
          tg_bot_database          postgres    false    216            �            1259    16473    stores    TABLE     �   CREATE TABLE tg_bot_database.stores (
    id integer NOT NULL,
    city character varying(25) NOT NULL,
    store character varying(55) NOT NULL
);
 #   DROP TABLE tg_bot_database.stores;
       tg_bot_database         heap    postgres    false    6                       0    0    TABLE stores    ACL     �   GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE tg_bot_database.stores TO tg_bot_raw_user;
GRANT SELECT ON TABLE tg_bot_database.stores TO power_bi_user;
          tg_bot_database          postgres    false    215            �            1259    16472    stores_id_seq    SEQUENCE     �   CREATE SEQUENCE tg_bot_database.stores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE tg_bot_database.stores_id_seq;
       tg_bot_database          postgres    false    6    215                       0    0    stores_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE tg_bot_database.stores_id_seq OWNED BY tg_bot_database.stores.id;
          tg_bot_database          postgres    false    214                       0    0    SEQUENCE stores_id_seq    ACL     �   GRANT ALL ON SEQUENCE tg_bot_database.stores_id_seq TO tg_bot_raw_user;
GRANT SELECT ON SEQUENCE tg_bot_database.stores_id_seq TO power_bi_user;
          tg_bot_database          postgres    false    214            �            1259    16409    users    TABLE     i  CREATE TABLE tg_bot_database.users (
    id integer NOT NULL,
    username_tg character varying(32) NOT NULL,
    full_name character varying(32) NOT NULL,
    office character varying(55) NOT NULL,
    rights character varying(12) NOT NULL,
    city character varying(20) NOT NULL,
    tg_user_id character varying(32),
    tg_chat_id character varying(32)
);
 "   DROP TABLE tg_bot_database.users;
       tg_bot_database         heap    postgres    false    6                       0    0    TABLE users    ACL     �  GRANT SELECT,INSERT,UPDATE ON TABLE tg_bot_database.users TO tg_bot WITH GRANT OPTION;
GRANT SELECT,INSERT ON TABLE tg_bot_database.users TO tg_bot_read_insert;
GRANT SELECT,INSERT,UPDATE ON TABLE tg_bot_database.users TO tg_bot_select_insert;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE tg_bot_database.users TO tg_bot_raw_user;
GRANT SELECT ON TABLE tg_bot_database.users TO power_bi_user;
          tg_bot_database          postgres    false    211            �            1259    16408    users_id_seq    SEQUENCE     �   CREATE SEQUENCE tg_bot_database.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE tg_bot_database.users_id_seq;
       tg_bot_database          postgres    false    211    6                       0    0    users_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE tg_bot_database.users_id_seq OWNED BY tg_bot_database.users.id;
          tg_bot_database          postgres    false    210                        0    0    SEQUENCE users_id_seq    ACL     �   GRANT SELECT ON SEQUENCE tg_bot_database.users_id_seq TO tg_bot_read_insert;
GRANT ALL ON SEQUENCE tg_bot_database.users_id_seq TO tg_bot_raw_user;
GRANT SELECT ON SEQUENCE tg_bot_database.users_id_seq TO power_bi_user;
          tg_bot_database          postgres    false    210            m           2604    16422    customer_numbers id    DEFAULT     �   ALTER TABLE ONLY tg_bot_database.customer_numbers ALTER COLUMN id SET DEFAULT nextval('tg_bot_database.customer_numbers_id_seq'::regclass);
 K   ALTER TABLE tg_bot_database.customer_numbers ALTER COLUMN id DROP DEFAULT;
       tg_bot_database          postgres    false    213    212    213            q           2604    16483    messages_from_users id    DEFAULT     �   ALTER TABLE ONLY tg_bot_database.messages_from_users ALTER COLUMN id SET DEFAULT nextval('tg_bot_database.messages_from_users_id_seq'::regclass);
 N   ALTER TABLE tg_bot_database.messages_from_users ALTER COLUMN id DROP DEFAULT;
       tg_bot_database          postgres    false    217    216    217            p           2604    16476 	   stores id    DEFAULT     x   ALTER TABLE ONLY tg_bot_database.stores ALTER COLUMN id SET DEFAULT nextval('tg_bot_database.stores_id_seq'::regclass);
 A   ALTER TABLE tg_bot_database.stores ALTER COLUMN id DROP DEFAULT;
       tg_bot_database          postgres    false    214    215    215            l           2604    16412    users id    DEFAULT     v   ALTER TABLE ONLY tg_bot_database.users ALTER COLUMN id SET DEFAULT nextval('tg_bot_database.users_id_seq'::regclass);
 @   ALTER TABLE tg_bot_database.users ALTER COLUMN id DROP DEFAULT;
       tg_bot_database          postgres    false    210    211    211                      0    16419    customer_numbers 
   TABLE DATA           �   COPY tg_bot_database.customer_numbers (id, customer_number, office, date, user_fullname, is_superapp_user, is_seen_in_last_90_days, city) FROM stdin;
    tg_bot_database          postgres    false    213   J6                 0    16480    messages_from_users 
   TABLE DATA           P   COPY tg_bot_database.messages_from_users (id, date, username, text) FROM stdin;
    tg_bot_database          postgres    false    217   7       
          0    16473    stores 
   TABLE DATA           :   COPY tg_bot_database.stores (id, city, store) FROM stdin;
    tg_bot_database          postgres    false    215   N>                 0    16409    users 
   TABLE DATA           r   COPY tg_bot_database.users (id, username_tg, full_name, office, rights, city, tg_user_id, tg_chat_id) FROM stdin;
    tg_bot_database          postgres    false    211   �@       !           0    0    customer_numbers_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('tg_bot_database.customer_numbers_id_seq', 33, true);
          tg_bot_database          postgres    false    212            "           0    0    messages_from_users_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('tg_bot_database.messages_from_users_id_seq', 206, true);
          tg_bot_database          postgres    false    216            #           0    0    stores_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('tg_bot_database.stores_id_seq', 38, true);
          tg_bot_database          postgres    false    214            $           0    0    users_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('tg_bot_database.users_id_seq', 27, true);
          tg_bot_database          postgres    false    210            u           2606    16426 &   customer_numbers customer_numbers_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY tg_bot_database.customer_numbers
    ADD CONSTRAINT customer_numbers_pkey PRIMARY KEY (id);
 Y   ALTER TABLE ONLY tg_bot_database.customer_numbers DROP CONSTRAINT customer_numbers_pkey;
       tg_bot_database            postgres    false    213            y           2606    16487 ,   messages_from_users messages_from_users_pkey 
   CONSTRAINT     s   ALTER TABLE ONLY tg_bot_database.messages_from_users
    ADD CONSTRAINT messages_from_users_pkey PRIMARY KEY (id);
 _   ALTER TABLE ONLY tg_bot_database.messages_from_users DROP CONSTRAINT messages_from_users_pkey;
       tg_bot_database            postgres    false    217            w           2606    16478    stores stores_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY tg_bot_database.stores
    ADD CONSTRAINT stores_pkey PRIMARY KEY (id);
 E   ALTER TABLE ONLY tg_bot_database.stores DROP CONSTRAINT stores_pkey;
       tg_bot_database            postgres    false    215            s           2606    16416    users users_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY tg_bot_database.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 C   ALTER TABLE ONLY tg_bot_database.users DROP CONSTRAINT users_pkey;
       tg_bot_database            postgres    false    211               �   x����
�@�������3����mO!�VtQ�IPO�&t5��#"�Z
ɶU�u�iڪ���k�ץ��9b�1���,�r���i�q������rx�?0	��hZ
K�	�����7�Ű��4,��%)�xŰ��B�0�&c�⍕M~����1�#� V��9W�h9���JX�i�A��@�         "  x���Mn7���S�V���ލ6ـ�8���X�X�F2FRk�m�Q�O!�(���4�c�,C�Q|Y,V�<Q�RO[�T���O�w���|9���?�&�Z�6
��Ӧ&�,4�&4(���5�-��Ӻ��
Mg�O�(t��5a`��'^\}��}u��y�j"�m,���$�]��r߉�x�P�|T��iD�ܴ#�D�Ҁr~~�~��|y�e�h�� ��N^���ώ^|�|��ĘF@�ϮW���� Ǥ4�T0�3�e0��ߞ�=|��������4�d�{���j~u��Ě���|q��]�cR�6��2�B�yH�X����
.���|�����j���&�d$W�` �6��5��N�IBZ�)������Z!4���|�&�)]U��&��l.M-�r̚��N��}�	�ō��������_���Z7�4�s�?��9�&`�s��wε���!x)��<C�r��*�Z�;����z��iqK�#s�����T�N��S�؊�W#p�L��#�6u+��F+J7�mQ�VjX�(m-�X��� j�Ҋ�D���RU=��++�=@f:����yee�䕔p(#@f:��ry%�յ���0�Cf:�9���ÿ�=�����6��B��{R�5Fu�:����{�!�\�LE��riQ�����˃u4�]�C����.��4�L�#¤�.�4=b��g;>M� �><2MO4=f�m�D�S=�9�6��TH���	�O��c�[���������*̀��<���e?��6L�@x֖�	��X^�����5�P��'?��^��NώN����i�][�O��@�#�Pv�l�H��nR��*�MZH]ۥ��> �<$Nx�l�%Β1�r	�����:���x�}��6�ե�SD�Yk'}�7��I�S$�}�)p�Y����B���կ���T�Vv��k}	�Ò��8av�MG&.-�vX�̥%�=�U�%�Ԣx�	v��՞���9bF�/-���&��K[B��mq%�K�y ��Q��Z��}�Q���(ew��ٽ��l�Zl�lv�֩�9���T�Q�p�);DY�rW��%ek��B���)�t=b�{fJ`�Z�ք]��xeM(BM��W�H[��v^)Bl�ζ�W� �ɳMav�H�Jv�el�+Z )#����DL{�� ��ހW?^|X��./����W��M�����$%���ݼ5���[��UC9oM�C�$�Λ�G�O��h��d~���Jr���vD�;���.园W6�z�����l8m����o#Rv��\�������K��.]��޵Oj���֍����~�h=%i*5F�.�'���ȈH.K��C1HNSVa�����AX$����G��t"�gu��A ��⠎�"93�0-����.$��v�	$��N ��x��T����Ǻ�ew�����XM3�98���H�1M[�Ɛ8�뱍��щ#�������b:za����3�v���?#<����7B"����O�=u���+�(���x���S� O��y耩dW:xb�M�m��	q�C�LXC����Y��e#�(S�9�J�@�V��+� �T��]	6�(���خ*�	�3�z�Ct���S�՝��:t��ґf��%<4�փ`��'ЪJC�\ۄ4�U�6�D�-�z�V�N�&?ft�v#4��Ig*��Ճ~�^�oЏ��� �P�_dű�`ЈRr ��Jc��X��i��A�i?b�c5h:�������봓ک��j�~ڌPXf������Aj'5�� �P�n4�����濒      
   ?  x���?o�@�g�O�/Ъ�!!c�JJT�Ru��X>s�l����R:t����.i���+�}��gL��t`{�{�%�I=葚�q�vJ���μSZ�~D��l������?���1��j�i�l����j�w��Ev�C�| �"�A�`�i֒>m҅�<p���Ed�	cP�M��a$}똑���n�5os���D��l� H�b�$��n����$��M���<����.�Ai	)��V���J��T-��ޡ�c����18J�%'��$so���������^$��aW�H�4w#k�;�l�}����pI�[laf	*��j��9���d\``�|�c=|���X��󳽆�d��p��~C�^��y>Nw�T��g N�I������p*O���JZ-~���M/����}�4@���Y��<S�f�c2`�E0Cՠ�;^�_ݚ���h$xϜ�>8��:����\�x�.�l����nL�6�Q�5�f_��|6���[2b�?�z+�4.Z��۲H�Y�Q6QG>�F����G7W��Gf�N�+b7X����9 ��g��         Z   x�3���--JLI�M,.I��r�v
v�ur�t��NN��Q�OK�LN-Vp��̭�H��/��M�KLO-�t��M,���"�=... �X_     