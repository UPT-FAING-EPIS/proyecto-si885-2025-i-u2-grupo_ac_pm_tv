SET QUOTED_IDENTIFIER ON;
GO
SET ANSI_NULLS ON;
GO

-- Crear base de datos analisistesis si no existe
IF NOT EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = 'analisistesis')
BEGIN
    CREATE DATABASE [analisistesis] COLLATE SQL_Latin1_General_CP1_CI_AS;
END
GO

USE [analisistesis];
GO

-- Tabla: archivo_csv
SET ANSI_NULLS ON;
GO
SET QUOTED_IDENTIFIER ON;
GO
CREATE TABLE [dbo].[archivo_csv](
	[id_archivo] [int] IDENTITY(1,1) NOT NULL,
	  NOT NULL,
	[fecha_subida] [datetime] NOT NULL CONSTRAINT DF_archivo_csv_fecha_subida DEFAULT GETDATE(),
	  NOT NULL,
PRIMARY KEY CLUSTERED ([id_archivo] ASC)
) ON [PRIMARY];
GO

-- Tabla: categoria_tecnologia
SET ANSI_NULLS ON;
GO
SET QUOTED_IDENTIFIER ON;
GO
CREATE TABLE [dbo].[categoria_tecnologia](
	[id_categoria] [int] IDENTITY(1,1) NOT NULL,
	  NOT NULL,
PRIMARY KEY CLUSTERED ([id_categoria] ASC)
) ON [PRIMARY];
GO

-- Tabla: tecnologia
SET ANSI_NULLS ON;
GO
SET QUOTED_IDENTIFIER ON;
GO
CREATE TABLE [dbo].[tecnologia](
	[id_tecnologia] [int] IDENTITY(1,1) NOT NULL,
	  NOT NULL,
	[id_categoria] [int] NULL,
PRIMARY KEY CLUSTERED ([id_tecnologia] ASC)
) ON [PRIMARY];
GO

-- Tabla: universidad
SET ANSI_NULLS ON;
GO
SET QUOTED_IDENTIFIER ON;
GO
CREATE TABLE [dbo].[universidad](
	[id_universidad] [int] IDENTITY(1,1) NOT NULL,
	  NOT NULL,
	  NOT NULL,
	  NOT NULL,
PRIMARY KEY CLUSTERED ([id_universidad] ASC)
) ON [PRIMARY];
GO

-- Tabla: tesis
SET ANSI_NULLS ON;
GO
SET QUOTED_IDENTIFIER ON;
GO
CREATE TABLE [dbo].[tesis](
	[id_tesis] [int] IDENTITY(1,1) NOT NULL,
	[ano_publicacion] [int] NULL,
	[categoria] [nvarchar](max) NULL,
	[id_universidad] [int] NULL,
	  NULL,
PRIMARY KEY CLUSTERED ([id_tesis] ASC)
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY];
GO

-- Tabla: tesis_tecnologia (relación N:M)
SET ANSI_NULLS ON;
GO
SET QUOTED_IDENTIFIER ON;
GO
CREATE TABLE [dbo].[tesis_tecnologia](
	[id_tesis] [int] NOT NULL,
	[id_tecnologia] [int] NOT NULL,
PRIMARY KEY CLUSTERED ([id_tesis] ASC, [id_tecnologia] ASC)
) ON [PRIMARY];
GO

-- Claves foráneas
ALTER TABLE [dbo].[tecnologia]  WITH CHECK ADD CONSTRAINT [fk_tecnologia_categoria]
FOREIGN KEY([id_categoria]) REFERENCES [dbo].[categoria_tecnologia] ([id_categoria])
ON DELETE SET NULL;
GO
ALTER TABLE [dbo].[tecnologia] CHECK CONSTRAINT [fk_tecnologia_categoria];
GO

ALTER TABLE [dbo].[tesis]  WITH CHECK ADD CONSTRAINT [fk_tesis_universidad]
FOREIGN KEY([id_universidad]) REFERENCES [dbo].[universidad] ([id_universidad])
ON DELETE SET NULL;
GO
ALTER TABLE [dbo].[tesis] CHECK CONSTRAINT [fk_tesis_universidad];
GO

ALTER TABLE [dbo].[tesis_tecnologia]  WITH CHECK ADD CONSTRAINT [fk_tesis_tecnologia_tecnologia]
FOREIGN KEY([id_tecnologia]) REFERENCES [dbo].[tecnologia] ([id_tecnologia]);
GO
ALTER TABLE [dbo].[tesis_tecnologia] CHECK CONSTRAINT [fk_tesis_tecnologia_tecnologia];
GO

ALTER TABLE [dbo].[tesis_tecnologia]  WITH CHECK ADD CONSTRAINT [fk_tesis_tecnologia_tesis]
FOREIGN KEY([id_tesis]) REFERENCES [dbo].[tesis] ([id_tesis]);
GO
ALTER TABLE [dbo].[tesis_tecnologia] CHECK CONSTRAINT [fk_tesis_tecnologia_tesis];
GO
