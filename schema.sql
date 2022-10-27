-- CREATE TABLE "public.Users" (
-- 	"id" serial NOT NULL,
-- 	"firstName" varchar(255) NOT NULL,
-- 	"lastName" varchar(255) NOT NULL,
-- 	"paswordHash" varchar(255) NOT NULL,
-- 	"email" varchar(255) NOT NULL,
-- 	"registeredAt" DATE NOT NULL,
-- 	"profile" TEXT NOT NULL,
-- 	CONSTRAINT "Users_pk" PRIMARY KEY ("id")
-- ) WITH (
--   OIDS=FALSE
-- );



-- CREATE TABLE "public.Boards" (
-- 	"id" serial NOT NULL,
-- 	"createdBy" serial NOT NULL,
-- 	"title" TEXT(255) NOT NULL,
-- 	"createdAt" TIMESTAMP NOT NULL,
-- 	"profile" TEXT(255) NOT NULL,
-- 	"content" TEXT(255) NOT NULL,
-- 	CONSTRAINT "Boards_pk" PRIMARY KEY ("id")
-- ) WITH (
--   OIDS=FALSE
-- );



-- CREATE TABLE "public.Posts" (
-- 	"id" serial NOT NULL,
-- 	"user_id" serial NOT NULL,
-- 	"content" TEXT(255) NOT NULL,
-- 	"createdAt" TIMESTAMP NOT NULL,
-- 	CONSTRAINT "Posts_pk" PRIMARY KEY ("id")
-- ) WITH (
--   OIDS=FALSE
-- );



-- CREATE TABLE "public.Liked_posts" (
-- 	"id" serial NOT NULL,
-- 	"posts_id" serial NOT NULL,
-- 	CONSTRAINT "Liked_posts_pk" PRIMARY KEY ("id")
-- ) WITH (
--   OIDS=FALSE
-- );



-- CREATE TABLE "public.Friends" (
-- 	"id" serial NOT NULL,
-- 	"source_id" serial NOT NULL,
-- 	"target_id" serial NOT NULL,
-- 	CONSTRAINT "Friends_pk" PRIMARY KEY ("id")
-- ) WITH (
--   OIDS=FALSE
-- );



-- CREATE TABLE "public.Messages" (
-- 	"id" serial NOT NULL,
-- 	"source_id" serial NOT NULL,
-- 	"target_id" serial NOT NULL,
-- 	"content" TEXT(255) NOT NULL,
-- 	CONSTRAINT "Messages_pk" PRIMARY KEY ("id")
-- ) WITH (
--   OIDS=FALSE
-- );



-- CREATE TABLE "public.Board_posts" (
-- 	"id" serial NOT NULL,
-- 	"board_id" serial NOT NULL,
-- 	"user_id" serial NOT NULL,
-- 	"content" TEXT(255) NOT NULL,
-- 	"createdAt" TIME NOT NULL,
-- 	CONSTRAINT "Board_posts_pk" PRIMARY KEY ("id")
-- ) WITH (
--   OIDS=FALSE
-- );



-- CREATE TABLE "public.Board_messages" (
-- 	"id" serial NOT NULL,
-- 	"board_id" serial NOT NULL,
-- 	"user_id" serial NOT NULL,
-- 	"content" TEXT(255) NOT NULL,
-- 	"createdAt" TIME NOT NULL,
-- 	CONSTRAINT "Board_messages_pk" PRIMARY KEY ("id")
-- ) WITH (
--   OIDS=FALSE
-- );



-- CREATE TABLE "public.Board_members" (
-- 	"id" serial NOT NULL,
-- 	"board_id" serial NOT NULL,
-- 	"user" serial NOT NULL,
-- 	CONSTRAINT "Board_members_pk" PRIMARY KEY ("id")
-- ) WITH (
--   OIDS=FALSE
-- );




-- ALTER TABLE "Boards" ADD CONSTRAINT "Boards_fk0" FOREIGN KEY ("createdBy") REFERENCES "Users"("id");
-- ALTER TABLE "Boards" ADD CONSTRAINT "Boards_fk1" FOREIGN KEY ("createdAt") REFERENCES "Users"("registeredAt");

-- ALTER TABLE "Posts" ADD CONSTRAINT "Posts_fk0" FOREIGN KEY ("user_id") REFERENCES "Users"("id");
-- ALTER TABLE "Posts" ADD CONSTRAINT "Posts_fk1" FOREIGN KEY ("createdAt") REFERENCES "Users"("registeredAt");

-- ALTER TABLE "Liked_posts" ADD CONSTRAINT "Liked_posts_fk0" FOREIGN KEY ("posts_id") REFERENCES "Posts"("id");

-- ALTER TABLE "Friends" ADD CONSTRAINT "Friends_fk0" FOREIGN KEY ("source_id") REFERENCES "Users"("id");
-- ALTER TABLE "Friends" ADD CONSTRAINT "Friends_fk1" FOREIGN KEY ("target_id") REFERENCES "Users"("id");

-- ALTER TABLE "Messages" ADD CONSTRAINT "Messages_fk0" FOREIGN KEY ("source_id") REFERENCES "Users"("id");
-- ALTER TABLE "Messages" ADD CONSTRAINT "Messages_fk1" FOREIGN KEY ("target_id") REFERENCES "Users"("id");

-- ALTER TABLE "Board_posts" ADD CONSTRAINT "Board_posts_fk0" FOREIGN KEY ("board_id") REFERENCES "Boards"("id");
-- ALTER TABLE "Board_posts" ADD CONSTRAINT "Board_posts_fk1" FOREIGN KEY ("user_id") REFERENCES "Users"("id");
-- ALTER TABLE "Board_posts" ADD CONSTRAINT "Board_posts_fk2" FOREIGN KEY ("createdAt") REFERENCES "Boards"("createdAt");

-- ALTER TABLE "Board_messages" ADD CONSTRAINT "Board_messages_fk0" FOREIGN KEY ("board_id") REFERENCES "Board_posts"("id");
-- ALTER TABLE "Board_messages" ADD CONSTRAINT "Board_messages_fk1" FOREIGN KEY ("user_id") REFERENCES "Users"("id");

-- ALTER TABLE "Board_members" ADD CONSTRAINT "Board_members_fk0" FOREIGN KEY ("board_id") REFERENCES "Boards"("id");
-- ALTER TABLE "Board_members" ADD CONSTRAINT "Board_members_fk1" FOREIGN KEY ("user") REFERENCES "Users"("id");









